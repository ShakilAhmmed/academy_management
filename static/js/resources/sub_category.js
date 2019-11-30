new Vue({
    el: "#sub_category",
    data: {
        slug: ''
    },
    methods: {
        ConvertSlug: function (event) {
            var text = event.target.value;
            text = text.toLowerCase().replace(/ /g, '-').replace(/[^\w-]+/g, '');
            $("#id_sub_category_slug").val(text);
            //this.slug = text;
        }
    },

    mounted() {

    }
});