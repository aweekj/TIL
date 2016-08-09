# Adding Disqus to Jekyll

## Prerequisite

1. Resister website to [Disqus](https://disqus.com).
2. Create a new Disqus site. For example, shortname.disqus.com.

## Install

Between a `{% if page.comments %}` and a `{% endif %}` tag, add the [Universal Embed Code](https://disqus.com/admin/universalcode/) in the appropriate template where you want.

```
{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables */
/*
var disqus_config = function () {
this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = '//{{ site.disqus.id }}.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
{% endif %}

```

Add Disqus Id to `_config.yml`
```yml
disqus:
  id: "YOUR_DISQUS_ID"
```


Add `comments` variable to the YAML frontmatter and set `true`. Comments can be disabled per-page by setting `comments: false` or by not including the comments option at all.

```md
---
layout: default
comments: true
# other options
---
```
