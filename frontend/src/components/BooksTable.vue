<template>
    <div class="container">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Title</th>
                    <th scope="col">Author</th>
                    <th scope="col">Rating</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="book in books">
                    <th scope="row">{{ book.id }}</th>
                    <td>{{ book.title }}</td>
                    <td>
                        <a href="#">{{ book.author.name }}</a>
                    </td>
                    <td>{{ book.rating }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    props: ['books']
}
</script>
