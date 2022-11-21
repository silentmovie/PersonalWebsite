---
layout: post
author: Bohan - [Learning Posts]
permalink: /2020/08/31/Sea-Ice-Dynamics-via-regularized-optimal-transport.html
image-slider: /assets/images/posts/parno-GRL2019.png
<!-- excerpt: Measuring Ice Motion with Optimal Transport -->
categories: blog
---

<h5><span style="color:#F58025">Measuring Ice Motion with Optimal Transport</span></h5>


<img class="img-fluid" src="{{site.baseurl}}/{{page.image-slider}}" alt="OT">

In \[[1]\], authors introduced a new way of estimating ice motion from satellite imagery using concepts from optimal transport.  The idea is to treat images as probability distributions and to leverage efficient regularized optimal transport algorithms to find a distance-minimizing transformation between images on two subsequent days.  From the transformation we can extract distances, velocities, and strains. However, this framework is limited to 2 marginals and the computational method introduces blurring due to the regularization parameter. This is the starting point of the recent project on the exact method to multimariginal optimal transport (MMOT) framework. 


----
##### References:


1. [Parno et al., Remote measurement of sea ice dynamics with regularized optimal transport, 2019](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2019GL083037)

[1]: https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2019GL083037
