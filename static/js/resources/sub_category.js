new Vue({
    el: "#sub_category",
    data: {
        slug: ''
    },
    methods: {
        ConvertSlug: function (event) {
            var text = event.target.value;
            text = text.toLowerCase().replace(/ /g, '-').replace(/[^\w-]+/g, '');
            this.slug = text;
        }
    },

    mounted() {
    }
});