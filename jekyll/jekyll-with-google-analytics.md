# Jekyll with Google Analytics

## Prerequisite

Sign in to [Google Analytics](https://www.google.com/analytics/), get Google Analytics ID.

## Usage

Insert below script in the `<head>` tag.

```html
<!-- Google Analytics -->
{% if site.google-analytics %}
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', '{{ site.google-analytics.id }}', 'auto');
ga('send', 'pageview');

</script>
{% endif %}
```

Insert below script in the `_config.yml` file.

```yml
google-analytics:
  id: "YOUR_GOOGLE_ANALYTICS_ID"

```
