<script>
    const fetchUsers = async () => {
        const res = await fetch("http://localhost:2000/user/");
        return await res.json();
    };

    const fetchMedia = async () => {
        const res = await fetch("http://localhost:2000/media/");
        return await res.json();
    };
</script>

<div class="flex flex-col h-screen justify-between">
    <div class="navbar mb-2 shadow-lg bg-neutral text-neutral-content">
        <div class="px-2 mx-2 navbar-start">
            <span class="text-lg font-bold"> DaisyUI </span>
        </div>
        <div class="hidden px-2 mx-2 navbar-center lg:flex">
            <div class="flex items-stretch">
                <!-- svelte-ignore a11y-missing-attribute -->
                <a href="/" class="btn btn-ghost btn-sm rounded-btn"> Home </a>
                <!-- svelte-ignore a11y-missing-attribute -->
                <a href="http://localhost:2000/docs" class="btn btn-ghost btn-sm rounded-btn"> API </a>
            </div>
        </div>
        <div class="navbar-end" />
    </div>
    <div class="mb-auto container mx-auto">
        <div class="overflow-x-auto">
            {#await fetchUsers()}
                Loading...
            {:then users}
                <table class="table w-full">
                    <thead>
                        <tr>
                            <th />
                            <th>Username</th>
                            <th>Email</th>
                            <th>Country ID</th>
                        </tr>
                    </thead>
                    {#each users as user}
                        <tbody>
                            <tr class="hover">
                                <th>{user.id}</th>
                                <td>{user.username}</td>
                                <td>{user.email}</td>
                                <td>{user.country_id}</td>
                            </tr>
                        </tbody>
                    {/each}
                </table>
            {:catch error}
                {error}
            {/await}
        </div>
        <div class="overflow-x-auto">
            {#await fetchMedia()}
                Loading...
            {:then medias}
                <table class="table w-full">
                    <thead>
                        <tr>
                            <th />
                            <th>Name</th>
                            <th>Media type</th>
                        </tr>
                    </thead>
                    {#each medias as media}
                        <tbody>
                            <tr class="hover">
                                <th>{media.id}</th>
                                <td>{media.name}</td>
                                <td>{media.media_type}</td>
                            </tr>
                        </tbody>
                    {/each}
                </table>
            {:catch error}
                {error}
            {/await}
        </div>
    </div>
</div>
