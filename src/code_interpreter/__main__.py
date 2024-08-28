# Copyright 2024 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
from datetime import timedelta

import aiorun
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from code_interpreter.application_context import ApplicationContext


async def main():
    ctx = ApplicationContext()
    
    loop = asyncio.get_event_loop()
    
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        lambda: loop.create_task(ctx.code_executor.cleanup_executors(timedelta(seconds=ctx.config.executor_max_idle_time))),
        "interval",
        seconds=ctx.config.executor_cleanup_interval,
    )
    scheduler.start()

    await ctx.grpc_server.start(listen_addr=ctx.config.grpc_listen_addr)

aiorun.run(main())