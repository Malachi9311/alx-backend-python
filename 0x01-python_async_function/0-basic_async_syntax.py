#!/usr/bin/env python3
"""
Module for task 00
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits random for a few seconds
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
