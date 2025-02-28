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
import contextlib
from typing import Any, Dict, Generator, Optional, Union

from torch import Tensor
from torch.nn import Module
from torch.optim import Optimizer

from lightning_lite.utilities.types import _PARAMETERS


class Precision:
    """Base class for all plugins handling the precision-specific parts of the training.

    The class attribute precision must be overwritten in child classes. The default value reflects fp32 training.
    """

    precision: Union[str, int] = 32

    @contextlib.contextmanager
    def forward_context(self) -> Generator[None, None, None]:
        """A contextmanager for managing model forward/training_step/evaluation_step/predict_step."""
        yield

    def pre_backward(self, tensor: Tensor, module: Optional[Module]) -> None:
        """Runs before precision plugin executes backward.

        Args:
            tensor: The tensor that will be used for backpropagation
            module: The module that was involved in producing the tensor and whose parameters need the gradients
        """

    def backward(self, tensor: Tensor, model: Optional[Module], *args: Any, **kwargs: Any) -> None:
        """Performs the actual backpropagation.

        Args:
            tensor: The tensor that will be used for backpropagation
            model: The module that was involved in producing the tensor and whose parameters need the gradients
        """
        tensor.backward(*args, **kwargs)

    def post_backward(self, tensor: Tensor, module: Optional[Module]) -> None:
        """Runs after precision plugin executes backward.

        Args:
            tensor: The tensor that will be used for backpropagation
            module: The module that was involved in producing the tensor and whose parameters need the gradients
        """

    def optimizer_step(
        self,
        optimizer: Optimizer,
        model: Optional[Module] = None,
        **kwargs: Any,
    ) -> Any:
        """Hook to run the optimizer step."""
        return optimizer.step(**kwargs)

    def get_main_params(self, optimizer: Optimizer) -> _PARAMETERS:
        """The main params of the model.

        Returns the plain model params here. Maybe different in other precision plugins.
        """
        for group in optimizer.param_groups:
            yield from group["params"]

    def state_dict(self) -> Dict[str, Any]:
        """Called when saving a checkpoint, implement to generate precision plugin state_dict.

        Returns:
            A dictionary containing precision plugin state.
        """
        return {}

    def load_state_dict(self, state_dict: Dict[str, Any]) -> None:
        """Called when loading a checkpoint, implement to reload precision plugin state given precision plugin
        state_dict.

        Args:
            state_dict: the precision plugin state returned by ``state_dict``.
        """
        pass

    def teardown(self) -> None:
        """This method is called to teardown the training process.

        It is the right place to release memory and free other resources.
        """
