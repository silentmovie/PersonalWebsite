---
layout: post
author: Bohan - [Research Posts]
permalink: /2022/08/05/Shape-Interpolation.html
image-slider: /assets/images/posts/barycenter-comp.png
<!-- excerpt: Multi-marginal optimal transport for the Wasserstein barycenter -->
categories: blog
excerpt_separator: <!--end_excerpt-->
---


<h5><span style="color:grey">Multi-marginal optimal transport for the Wasserstein barycenter</span></h5>
<!--end_excerpt-->

<div><img class="img-fluid" src="{{site.baseurl}}/{{page.image-slider}}" alt="Wasserstein Barycenter" /></div>

A barycenter-type of problems is: given a set of objects $(\mu_i)_{i=1}^m$,  we are looking for something in the same space (or formally speaking: within the same category), which is close to those objects with respect to some distance.

\begin{equation}
\label{eq:bary}
\mu= \textrm{argmin}\sum_{i=1}^m \lambda_i \textrm{dis}(\mu_i,\mu).
\end{equation}

Depending on the metric, the barycenter contains "averaged" information from objects.

In our problem, we are particularly interested in the space of probability measures equipped with the Wasserstein distance, which was introduced by Agueh and Carlier \[[1]\].

\begin{equation}
\label{eq:Wass_bary}
\mu= \textrm{argmin}\sum_{i=1}^m \frac{\lambda_i}{2} W_2^2(\mu_i,\mu).
\end{equation}

They showed it is equivalent to the MMOT under the cost 
\begin{equation}
c(x_1,\cdots,x_m)=\sum_{i<j}\frac{\lambda_i \lambda_j}{2} \|x_i-x_j\|^2.
\end{equation}

And the Wasserstein barycenter is introduced by
\begin{equation}
\label{eq:pushforward}
\mu= (\textrm{id} - \frac{\nabla f_i}{\lambda_i})_{\sharp} \mu_i.
\end{equation}

Our method \[[2]\] provides an exact and efficient way to compute dual variables $(f_i)$ in an indirect way because the cost $c(x_1,\cdots,x_m)=\sum_{i<j}\frac{\lambda_i \lambda_j}{2} \|x_i-x_j\|^2$ corresponds to a complete graph: we find the dual variables $(\hat{f_i})$ to an equivalent MMOT in a tree and use those dual variables to recover the original dual variables $(f_i)$

----
##### References:


1. [Agueh and Carlier, Barycenter in the Wasserstein space, 2011.](http://doi.org/10.1137/100805741)
2. [Zhou and Parno, Efficient and Exact Multimarginal Optimal Transport with Pairwise Costs, 2022.](https://arxiv.org/abs/2208.03025)


[1]: http://doi.org/10.1137/100805741
[2]: https://arxiv.org/abs/2208.03025




