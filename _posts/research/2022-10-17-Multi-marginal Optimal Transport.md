---
layout: post
author: Bohan Zhou
permalink: /2020/10/17/Ice-floe.html
image-slider: /assets/images/posts/Bohan_icefloe.gif
excerpt: Multi-marginal optimal transport for Ice Floe Prediction
categories: blog
---

<img class="img-fluid" src="{{site.baseurl}}/{{page.image-slider}}" alt="OT">

B. Zhou and M. Parno are working on a general multi-marginal optimal transport (MMOT) framework to obtain the continuous representation of discrete-in-time data. Given observations (called as marginals), our algorithm provides a prediction on the sea ice dynamics in a continuous time. This provides a solution to some stage in the [Lagrangian Observation Mapping](https://simda-muri.github.io/challenges/source/descriptions/problem2.html). The python package with its description can be found [here](https://simda-muri.github.io/mmot/).

Using the SAR data (every 6 days) obtained from [Alaska Satellite Facility](https://asf.alaska.edu) on the Robertson Channel (thanks to J. Park), the video shows the prediction dynamics every 2 day.
