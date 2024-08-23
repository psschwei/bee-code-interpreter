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

from typing import Annotated, TypeAliasType

from pydantic import Field

ExecutorId = TypeAliasType(
    "ExecutorId", Annotated[str, Field(pattern=r"^[a-z0-9-]{1,32}$")]
)
Hash = TypeAliasType("Hash", Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")])
AbsolutePath = TypeAliasType(
    "AbsolutePath", Annotated[str, Field(pattern=r"^/[^/].*$")]
)
