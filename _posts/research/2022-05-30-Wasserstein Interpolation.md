---
layout: post
author: Bohan and Tyler - [Undergraduate Research Posts]
permalink: /2022/05/30/Understand-interpolation.html
image-slider: /assets/images/posts/Wass-dough.gif
categories: blog
excerpt_separator: <!--end_excerpt-->
---


<h5><span style="color:#00703C">Wasserstein Interpolation Examples in Point Clouds</span></h5>
<!--end_excerpt-->
<div class="row">
	<div class="column">
	<img class="img-fluid" src="{{site.baseurl}}//assets/images/posts/Wass-dough.gif" alt="Wasserstein dough">
	</div>
		<div class="column">
	<img class="img-fluid" src="{{site.baseurl}}//assets/images/posts/Wass-rotation.gif" alt="Wasserstein rotation">
	</div>
</div>

Tyler, an undergraduate student at Dartmouth College, wants to fully understand the Wasserstein interpolation. Though the Wasserstein interpolation is not a new stuff: between two given measures $\mu_1$ and $\mu_2$, one may define the Wasserstein interpolation through either a given optimal transport map $T$:

\begin{equation}
\label{eq:Wass_int_map}
\mu_t = ((1-t)x+tT(x))_{\sharp}\mu_1;
\end{equation}

or a given optimal transport plan $P$:

\begin{equation}
\label{eq:Wass_int_plan}
\mu_t = ((1-t)x+ty)_{\sharp} P.
\end{equation}

However, as shown in the above animation figures, the Wasserstein interpolation is not that stable: Given two sets of two point clouds (blue point cloud at time 0 and red point cloud at time 1). On the left plot, they are in 90 degree intersected at their ends; on the right plot, they are in 84.55 degree intersected at their ends. However their interpolation behaviors via the Wasserstein interpolation look quite different. The left one is analogous with deformations of doughs in the bakery, the right one is almost regular rotation of a baguette. 

In this particular example, we can explain it via optimal transport theory while there is still a long way towards a full understanding on the Wasserstein interpolation, so that predictions based on the Wasserstein interpolation are controlable.

Our current code owes a debt of gratitute to Prof. Peyre's open-resource online experiments \[[1]\], in particular, the linear programming to OT. In the future, we plan to use more recent faster solver \[[2]\], or more general MMOT solver \[[3]\]. 

----
##### References:


1. [Peyre, Numerical Tours.](https://www.numerical-tours.com/python/)
2. [Jacobs and Leger, The Back-and-Forth Method, 2020.](https://back-and-forth.netlify.app)
3. [Parno and Zhou, MMOT2D python package, 2022.](https://simda-muri.github.io/mmot/)

[1]: https://www.numerical-tours.com/python/
[2]: https://back-and-forth.netlify.app
[3]: https://simda-muri.github.io/mmot/


