---
layout: default
title: "People"
---


<div class="container">

      {% for cat in site.data.people %}
          <hr>
          <h2> {{ cat.title }} </h2>
          <div class="row">

            {% for person in cat.people %}
              <div class="col-lg-4 mb-4 mt-4">

                <div class="card text-center">
                  <div class="card-header">
                    <h3> <a href="{{ person.website }}" style="color:#000000;">{{ person.name }}</a> </h3>
                  </div>
                  <div class="card-body">
                    <a href="{{ person.website }}" ><img src="{{ site.baseurl }}/assets/images/{{ person.image }}" alt="{{ person.name }}" height="150" /></a>
                    <br>
                    {{ person.text }}
                  </div>
                </div>
              </div>
            {% endfor %}
          </div>

      {% endfor %}

</div>
