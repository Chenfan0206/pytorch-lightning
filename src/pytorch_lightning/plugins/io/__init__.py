# Copyright The PyTorch Lightning team.
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
from lightning_lite.plugins.io.checkpoint_plugin import CheckpointIO
from lightning_lite.plugins.io.torch_plugin import TorchCheckpointIO
from lightning_lite.plugins.io.xla_plugin import XLACheckpointIO
from pytorch_lightning.plugins.io.async_plugin import AsyncCheckpointIO
from pytorch_lightning.plugins.io.hpu_plugin import HPUCheckpointIO

__all__ = ["AsyncCheckpointIO", "CheckpointIO", "HPUCheckpointIO", "TorchCheckpointIO", "XLACheckpointIO"]
