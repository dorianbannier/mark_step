# mark_step

Function allowing to automatically mark the foot contact/strike and the foot off in the current trial opened in the Vicon Nexus software.

In order to use the function mark_step(), it is crucial to correctly installing the Vicon Nexus SDK. Then, you can add the folder containing the function to your path, in order use it as follows.

## Get started

The use of mark_step is basic:

``` python
import mark_step as ms

ms.mark_step()
```

Each time you open a trial in Vicon Nexus, you simple had to execute the mark_step() command. That's all.
In order to help in checking if the marking is accurate, it is possible to ask to the function to draw a plot of the heel movement and to place on it the foot contact and foot off it detected:

``` python
ms.mark_step(plot = 1)
```
By default, the script uses the 'LHEE' and 'RHEE' markers. If you want to use other markers to automatically mark the event's steps:

``` python
ms.mark_step(marker_left = 'LTOE', marker_right = 'RTOE')
```

