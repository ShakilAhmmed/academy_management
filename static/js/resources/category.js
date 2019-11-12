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
        AllData: [],
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
                        _this.AllData.push(data.data);
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
                _this.CategoryForm[key] = '';
            });
        },
        ConvertSlug: function (event) {
            var text = event.target.value;
            text = text.toLowerCase().replace(/ /g, '-').replace(/[^\w-]+/g, '');
            this.CategoryForm.category_slug = text;
        },
        GetCategoryData: function () {
            const _this = this;
            $.ajax({
                url: 'add_category',
                type: "GET",
                success: function (data) {
                    console.log(data);
                    _this.AllData = data;
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.log(textStatus, errorThrown);
                }
            });
        },
        DeleteCategory: function (index, id) {
            const _this = this;
            const URL = 'category_detail/' + id;
            swal({
                title: "Are you sure?",
                text: "Are you Sure Delete This",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            })
                .then((willDelete) => {
                    if (willDelete) {
                        $.ajax({
                            url: URL,
                            type: "DELETE",
                            success: function (response) {
                                if (response.status === 204) {
                                    _this.AllData.splice(index, 1);
                                    toastr.warning('Success!', 'Category Deleted Successfully!');
                                } else {
                                    toastr.info('Opps!', 'Please Try Again Later');
                                }
                            },
                            error: function (jqXHR, textStatus, errorThrown) {
                                toastr.info('Opps!', 'Application Error');
                                console.log(textStatus, errorThrown);
                            }
                        });
                    }
                });
        },
        StatusChange: function (id) {
            const _this = this;
            $.ajax({
                url: 'category_status/' + id,
                type: "GET",
                success: function (data) {
                    if (data.status === 203) {
                        toastr.success('Success!', 'Status Changed Into Active');
                    } else {
                        toastr.warning('Success!', 'Status Changed Into Inactive');
                    }
                    _this.GetCategoryData();
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.log(textStatus, errorThrown);
                }
            });

        }
    },

    mounted() {
        this.GetCategoryData();
        console.log("Ok")
    }
});