<script>
    const logSmth = async (input) => {
        console.log(input);
    }

    const fetchDocuments = async () => {
        const res = await fetch("http://localhost:2000/document/");
        return await res.json();
    };
</script>

<h1>Hey</h1>

{#await fetchDocuments()}
    Loading...
{:then document}
    Document: {document.data}
{:catch error}
    {error}
{/await}
