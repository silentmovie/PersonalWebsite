---
layout: post
author: Bohan
permalink: /2020/08/31/Sea-Ice-Dynamics-via-regularized-optimal-transport.html
image-slider: /assets/images/posts/parno-GRL2019.png
excerpt: Measuring Ice Motion with Optimal Transport
categories: blog
---

<img class="img-fluid" src="{{site.baseurl}}/{{page.image-slider}}" alt="OT">

In [Parno et al. (2019)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2019GL083037), we introduced a new way of estimating ice motion from satellite imagery using concepts from optimal transport.  The idea is to treat images as probability distributions and to leverage efficient regularized optimal transport algorithms to find a distance-minimizing transformation between images on subsequent days.  From the transformation we can extract distances, velocities, and strains.