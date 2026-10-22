<script>
  let result = 'Loading...';

  fetch('/api/')
    .then((response) => response.json())
    .then((data) => {
      result = data.message;
    })
    .catch((error) => {
      result = `Error: ${error.message}`;
    });
</script>

<section>
  <h1>{result}</h1>
  <h2>Skeleton Svelte + FastAPI app</h2>
</section>
