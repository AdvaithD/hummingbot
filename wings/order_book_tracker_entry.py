#!/usr/bin/env python

from typing import Dict
from wings.order_book import OrderBook
from wings.ddex_active_order_tracker import DDEXActiveOrderTracker
from wings.radar_relay_active_order_tracker import RadarRelayActiveOrderTracker


class OrderBookTrackerEntry:
    def __init__(self, symbol: str, timestamp: float, order_book: OrderBook):
        self._symbol = symbol
        self._timestamp = timestamp
        self._order_book = order_book

    def __repr__(self) -> str:
        return f"OrderBookTrackerEntry(symbol='{self._symbol}', timestamp='{self._timestamp}', " \
            f"order_book='{self._order_book}')"

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def timestamp(self) -> float:
        return self._timestamp

    @property
    def order_book(self) -> OrderBook:
        return self._order_book


class DDEXOrderBookTrackerEntry(OrderBookTrackerEntry):
    def __init__(self, symbol: str, timestamp: float, order_book: OrderBook,
                 active_order_tracker: DDEXActiveOrderTracker):

        self._active_order_tracker = active_order_tracker
        super(DDEXOrderBookTrackerEntry, self).__init__(symbol, timestamp, order_book)

    def __repr__(self) -> str:
        return f"DDEXOrderBookTrackerEntry(symbol='{self._symbol}', timestamp='{self._timestamp}', " \
            f"order_book='{self._order_book}')"

    @property
    def active_order_tracker(self) -> DDEXActiveOrderTracker:
        return self._active_order_tracker


class RadarRelayOrderBookTrackerEntry(OrderBookTrackerEntry):
    def __init__(self, symbol: str, timestamp: float, order_book: OrderBook,
                 active_order_tracker: RadarRelayActiveOrderTracker):

        self._active_order_tracker = active_order_tracker
        super(RadarRelayOrderBookTrackerEntry, self).__init__(symbol, timestamp, order_book)

    def __repr__(self) -> str:
        return f"RadarRelayOrderBookTrackerEntry(symbol='{self._symbol}', timestamp='{self._timestamp}', " \
            f"order_book='{self._order_book}')"

    @property
    def active_order_tracker(self) -> RadarRelayActiveOrderTracker:
        return self._active_order_tracker

