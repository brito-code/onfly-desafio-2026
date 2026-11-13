"""Política de status das reservas."""

from __future__ import annotations


_BILLABLE_STATUSES = frozenset({"CONFIRMED"})


def is_billable(status: str) -> bool:
    """Indica se a reserva entra nos totais financeiros e de noites."""
    return status in _BILLABLE_STATUSES
