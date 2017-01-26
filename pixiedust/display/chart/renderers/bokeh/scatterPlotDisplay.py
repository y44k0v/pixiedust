# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2017
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

from pixiedust.display.chart.renderers import PixiedustRenderer
from .bokehBaseDisplay import BokehBaseDisplay
import pixiedust
from bokeh.charts import Scatter

myLogger = pixiedust.getLogger(__name__)

@PixiedustRenderer(id="scatterPlot")
class ScatterPlotRenderer(BokehBaseDisplay):

    def createBokehChart(self):
        
        pandaList = self.getPandasValueFieldValueLists()
        data = pandaList[0] if len(pandaList) >= 1 else []
       
        return Scatter(data, xlabel="/".join(self.getKeyFields()),ylabel="/".join(self.getValueFields()),legend=None, plot_width=800)