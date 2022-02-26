{% include "blurb.md" %}

# Projects

<table style="width:100%; text-align:center; border:none; table-layout: fixed">
  <colgroup>
    <col style="max-width:25%">
    <col style="max-width:25%">
    <col style="max-width:25%">
    <col style="max-width:25%">
  </colgroup>
  <tbody>
    {% for row in rows -%}
    <tr>
      {% for project in row -%}
        <td width="25%" align="center"><a href="{{project.repo_url}}" width="100%"><img src="{{project.img_url}}"></img></a></td>{{"
      " if not loop.last}}
      {%- endfor %}
    </tr>
    <tr>
      {% for project in row -%}
        <td align="center">{{project.description}}</td>{{"
      " if not loop.last}}
      {%- endfor %}
    </tr>
    {% endfor -%}
  </tbody>
</table>