---
layout: post
author: Bohan - [Research Posts]
permalink: /2022/10/17/Robertson-Channel.html
image-slider: /assets/images/posts/Bohan_icefloe.gif
<!-- excerpt: Multi-marginal optimal transport for Sea Ice Dynamics Prediction -->
categories: blog
excerpt_separator: <!--end_excerpt-->
---


<h5><span style="color:grey">Multi-marginal Optimal Transport for Sea Ice Dynamics Prediction</span></h5>
<!--end_excerpt-->

<img class="img-fluid" src="{{site.baseurl}}/{{page.image-slider}}" alt="Robertson Channel">

B. Zhou and M. Parno \[[1]\] utilize a general multi-marginal optimal transport (MMOT) framework to obtain the continuous representation of discrete-in-time data. One possible application is the prediction on the sea ice dynamics. Given observations (called as marginals in the general framework) at different time-stamps, our method provides a prediction on the sea ice dynamics in a continuous time. This provides a solution to some stage in the [Lagrangian Observation Mapping](https://simda-muri.github.io/challenges/source/descriptions/problem2.html). The python package with its description can be found \[[2]\].

Using the SAR data (every 6 days) obtained from [Alaska Satellite Facility](https://asf.alaska.edu) on the Robertson Channel (thanks to our group member J. Park at Dartmouth), the video shows the prediction dynamics every 2 day. Even finer predictions are possible within a few minutes on a personal computer.

----
##### References:

1. [Zhou and Parno, Efficient and Exact Multimarginal Optimal Transport with Pairwise Costs, 2022.](https://arxiv.org/abs/2208.03025)
2. [Parno and Zhou, MMOT2D python package, 2022.](https://simda-muri.github.io/mmot/)


[1]: https://arxiv.org/abs/2208.03025
[2]: https://simda-muri.github.io/mmot/


