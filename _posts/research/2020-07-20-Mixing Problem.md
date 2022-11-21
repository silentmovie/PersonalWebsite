---
layout: post
author: Bohan - [Research Posts]
permalink: /2020/07/20/RT.html
image-slider: /assets/images/posts/movie6.png
categories: blog
excerpt_separator: <!--end_excerpt-->
---


<h5><span style="color:grey">Mixing under Rayleigh-Taylor instability</span></h5>
<!--end_excerpt-->

<div class="row">
<img class="img-fluid" src="{{site.baseurl}}//assets/images/posts/zmodel.mov" alt="Zmodel">
</div>

This project is a follow-up to the paper \[[1]\]. In that paper, authors derived an asymptotic model for the motion of multiphase incompressible Euler flows in 2D, subjected to Rayleigh-Taylor(RT) instability, allowing turn-over.

Matlab codes in \[[2]\] simulates the mixing phenomenon caused by RT even for immiscible fluids without diffusion. To see how to measure mixedness without diffusion, see \[[3]\].

In the movie, the top box simulates the "rocket rig" experiment (mixing of NaI solution and pentane using rocket motors), in an ensemble averaging procedure; the second box shows the occupied density in the zoom-in window averaged in all experiments; the third box shows the evolution of the mixedness in terms of $\dot{H}^{-1}$ norm; the fourth box shows the effect of artificial viscosity.

Please refer to \[[4]\] for the recent development.

----
##### References:


1. [Granero-Belinchon and Shkoller, A model for Rayleigh-Taylor mixing and interface turn-over, 2017.](https://epubs.siam.org/doi/pdf/10.1137/16M1083463?casa_token=0dRxZ_jt06AAAAAA:T2Bgm0RnBw64UHFZygEuj4gScaPw01fnfWQU0APePKiajut4Bui_B03K4PeqUFfZ85MaITV9ow)
2. [Zhou, RTmodel, 2020.](https://github.com/silentmovie/RTmodel)
3. [Thiffeault, Using multiscale norms to quantify mixing and transport, 2011.](https://iopscience.iop.org/article/10.1088/0951-7715/25/2/R1/pdf?casa_token=kxRedMFYm1QAAAAA:jtsmOCS0mceHwfRLlOsfEvV5YVVmZj-HNqMCKgyXhoac7HOUkUaKnyfEQlOruM9SJ1dL54_R1Q)
4. [Pandya and Shkoller, 3D interface models for Rayleigh-Taylor Problems, 2022.](https://arxiv.org/abs/2201.04538)


[1]: https://epubs.siam.org/doi/pdf/10.1137/16M1083463?casa_token=0dRxZ_jt06AAAAAA:T2Bgm0RnBw64UHFZygEuj4gScaPw01fnfWQU0APePKiajut4Bui_B03K4PeqUFfZ85MaITV9ow
[2]: https://github.com/silentmovie/RTmodel
[3]: https://simda-muri.github.io/mmot/
[4]: https://arxiv.org/abs/2201.04538


