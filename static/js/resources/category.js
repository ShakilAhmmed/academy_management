new Vue({
    el: "#category",
    data: {
        CategoryForm: {
            category_code: '',
            category_title: '',
            category_slug: '',
            category_status: '',
            csrfmiddlewaretoken: csrf,
        },
        errors: new Errors(),
    },
    methods: {
        AddNewCategory: function () {
            const _this = this;
            $.ajax({
                url: 'add_category',
                type: "POST",
                data: _this.CategoryForm,
                success: function (data) {
                    if (data.status === 201) {
                        toastr.success('Success!', 'New Category Created Successfully');
                        _this.ClearData();
                        $(".close").click();
                    } else {
                        _this.errors.record(data.errors);
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.log(textStatus, errorThrown);
                }
            });

        },
        ClearData: function () {
            const _this = this;
            _this.errors.record([]);
            $.each(_this.CategoryForm, function (key, value) {
                _this.CategoryForm[key]='';
            });
        },
        ConvertSlug: function (event) {
            var text = event.target.value;
            text = text.toLowerCase().replace(/ /g, '-').replace(/[^\w-]+/g, '');
            this.CategoryForm.category_slug = text;
        },
    },

    mounted() {
        console.log("Ok")
    }
});