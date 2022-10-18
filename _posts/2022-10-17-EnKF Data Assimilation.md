---
layout: post
author: Max Ramgraber
permalink: /2020/10/17/EnKF-data-assimilation.html
image-slider: /assets/images/posts/Max_DA.gif
excerpt: Ice Thickness Data Assimilation
categories: blog
---

<img class="img-fluid" src="{{site.baseurl}}/{{page.image-slider}}" alt="OT">

Data assimilation for a synthetic sea ice model using the Ensemble Kalman Filter (EnKF). The setting consists of a thick ice sheet towards the right and left boundaries, divided by a thin ice sheet in the center. Wind of varying strength and direction acts as a known forcing. We make regular noisy observations and neglect forecast error. The ensemble state uncertainty (grey bands) quickly narrows around the synthetic true state (dashed red line).
