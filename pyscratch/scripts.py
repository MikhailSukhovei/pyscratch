from __future__ import annotations

import ast
import inspect
import textwrap
from collections.abc import Callable, Iterator
from functools import wraps
from typing import Any


_RUN_VALUE_NAME = "__pyscratch_run_value"


def _run_value(value: object) -> Iterator[None]:
    if hasattr(value, "run"):
        yield from value.run()  # type: ignore[attr-defined]
    elif isinstance(value, Iterator):
        yield from value


def _yield_once(location: ast.AST) -> ast.Expr:
    node = ast.Expr(value=ast.Yield(value=ast.Constant(value=None)))
    return ast.copy_location(node, location)


class _ScriptTransformer(ast.NodeTransformer):
    def __init__(self) -> None:
        self._function_depth = 0

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        if self._function_depth > 0:
            return node

        self._function_depth += 1
        try:
            node.decorator_list = []
            node.body = self._visit_statements(node.body)
            node.body.append(self._force_generator_node(node))
            return node
        finally:
            self._function_depth -= 1

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
        return node

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:
        return node

    def visit_Expr(self, node: ast.Expr) -> ast.AST:
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            return node

        value = self.visit(node.value)
        run_call = ast.Call(
            func=ast.Name(id=_RUN_VALUE_NAME, ctx=ast.Load()),
            args=[value],
            keywords=[],
        )
        return ast.copy_location(ast.Expr(value=ast.YieldFrom(value=run_call)), node)

    def visit_Return(self, node: ast.Return) -> ast.AST | list[ast.AST]:
        if node.value is None:
            return node

        value = self.visit(node.value)
        run_call = ast.Call(
            func=ast.Name(id=_RUN_VALUE_NAME, ctx=ast.Load()),
            args=[value],
            keywords=[],
        )
        run_node = ast.copy_location(ast.Expr(value=ast.YieldFrom(value=run_call)), node)
        return_node = ast.copy_location(ast.Return(value=None), node)
        return [run_node, return_node]

    def visit_While(self, node: ast.While) -> ast.AST:
        node.test = self.visit(node.test)
        node.body = self._visit_statements(node.body)
        node.body.append(_yield_once(node))
        node.orelse = self._visit_statements(node.orelse)
        return node

    def visit_For(self, node: ast.For) -> ast.AST:
        node.target = self.visit(node.target)
        node.iter = self.visit(node.iter)
        node.body = self._visit_statements(node.body)
        node.body.append(_yield_once(node))
        node.orelse = self._visit_statements(node.orelse)
        return node

    def visit_AsyncFor(self, node: ast.AsyncFor) -> ast.AST:
        return node

    def visit_Continue(self, node: ast.Continue) -> list[ast.AST]:
        return [_yield_once(node), node]

    def _visit_statements(self, statements: list[ast.stmt]) -> list[ast.stmt]:
        transformed: list[ast.stmt] = []
        for statement in statements:
            result = self.visit(statement)
            if result is None:
                continue
            if isinstance(result, list):
                transformed.extend(result)
            else:
                transformed.append(result)
        return transformed

    def _force_generator_node(self, location: ast.AST) -> ast.If:
        node = ast.If(
            test=ast.Constant(value=False),
            body=[_yield_once(location)],
            orelse=[],
        )
        return ast.copy_location(node, location)


def script(function: Callable[..., Any]) -> Callable[..., Any]:
    compiled = _compile_function(function)

    @wraps(function)
    def wrapper(*args: object, **kwargs: object) -> object:
        return compiled(*args, **kwargs)

    return wrapper


def _compile_function(function: Callable[..., Any]) -> Callable[..., Any]:
    try:
        source = textwrap.dedent(inspect.getsource(function))
    except (OSError, TypeError):
        return function

    module = ast.parse(source)
    function_nodes = [
        node for node in module.body if isinstance(node, ast.FunctionDef)
    ]
    if len(function_nodes) != 1:
        return function

    transformed = _ScriptTransformer().visit(module)
    ast.fix_missing_locations(transformed)

    namespace = _function_namespace(function)
    code = compile(transformed, inspect.getsourcefile(function) or "<pyscratch-script>", "exec")
    exec(code, namespace)
    compiled = namespace[function.__name__]
    return compiled


def _function_namespace(function: Callable[..., Any]) -> dict[str, object]:
    namespace: dict[str, object] = dict(function.__globals__)
    closure = inspect.getclosurevars(function)
    namespace.update(closure.globals)
    namespace.update(closure.nonlocals)
    namespace[_RUN_VALUE_NAME] = _run_value
    return namespace
