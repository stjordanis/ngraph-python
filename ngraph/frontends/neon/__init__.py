# ----------------------------------------------------------------------------
# Copyright 2016 Nervana Systems Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

# commonly used modules.  Should these still be imported in neon frontend?
from ngraph.op_graph.axes import Axes
from ngraph.frontends.neon.axis import ax
from ngraph.frontends.neon.activation import Rectlin, Identity, Explin, Normalizer, Softmax, Tanh, \
    Logistic
from ngraph.frontends.neon.argparser import NgraphArgparser
from ngraph.frontends.neon.callbacks import *
from ngraph.frontends.neon.cost import CrossEntropyBinary, CrossEntropyMulti, SumSquared, \
    Misclassification
from ngraph.frontends.neon.layer import *
from ngraph.frontends.neon.model import Model
from ngraph.frontends.neon.optimizer import *

# include Axes here because old 2.0 code needs to be updated to include Axes
# annotations in the call to model.fit.
# TODO: deprecate this Axes, you should just use be.Axes instead

# old neon code which hasn't changed but should be available in this namespace
# TODO: there are a lot of classes which are similar to the ones listed here,
# but are not listed here and probably should be.