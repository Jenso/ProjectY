$.ajaxSetup({
    cache: false
});

window.global_filter = '[]';

var InspirationImage = Backbone.Model.extend({
});


var PinsPagerCollection = Backbone.Paginator.requestPager.extend({
    model:InspirationImage,
    paginator_core: {
        // the type of the request (GET by default)
        type: 'GET',

        // the type of reply (jsonp by default)
        dataType: 'jsonp',

        // the URL (or base URL) for the service
        // Set by the django template
        url: "/api/pin/",
    },
    paginator_ui: {
        // the lowest page index your API allows to be accessed
        firstPage: 0,

        // which page should the paginator start from
        // (also, the actual page the paginator is on)
        currentPage: 0,

        // how many items per page should be shown
        perPage: 10,

        // a default number of total pages to query in case the API or
        // service you are using does not support providing the total
        // number of pages for us.
        // 10 as a default in case your service doesn't return the total
        totalPages: 10
    },
    server_api: {
        // number of items to return per request/page
        'limit': function() { return this.perPage },
        'category': function() {
            // FIXME: the filter shouldnt be set with a global variable...
            return window.global_filter
        },

        // how many results the request should skip ahead to
        'offset': function() { return this.currentPage * this.perPage },
    },
    parse: function (response) {
        // Be sure to change this based on how your results
        // are structured (e.g d.results is Netflix specific)
        var tags = response.objects;

        // number of pages with content
        this.totalPages = Math.floor((response.meta.total_count - 1) / this.perPage);
        return tags;
    }
});


Pinry = new Backbone.Marionette.Application();

Pinry.addRegions({
    mainRegion: "#pins"
});


PinsCollection = Backbone.Collection.extend({
    url: '/api/pin/',
});

var PinOverlayView = Backbone.Marionette.ItemView.extend({
    template: '#tpl-pin-overlay',
    className: 'product-overlay',
    events: {
        'click .more-info': 'moreInfo',
        'click .buy': 'buy',
    },
    moreInfo: function() {
	_kmq.push(['record', 'Image overlay - click mer info']);
        _gaq.push(["_trackEvent", "Image overlay", "Click - mer info"]);
    },
    buy: function() {
	_kmq.push(['record', 'Image overlay - click buy']);
        _gaq.push(["_trackEvent", "Image overlay", "Click - buy"])
    },
    onRender: function() {
        this.$el.attr('id', this.model.get("id"));
    }
});

var PinView = Backbone.Marionette.ItemView.extend({
    template: "#tpl-pin",
    className: "pin",
    events: {
        'click': 'pinOverlay',
    },
    pinOverlay: function() {
        var pinOverlay = new PinOverlayView({model: this.model}).render();
        // FIXME: is this really a good way to add it to the div?
        this.$el.append(pinOverlay.$el);
    },
});

var PinsView = Backbone.Marionette.CollectionView.extend({
    handler: null,
    itemView: PinView,
    isLoading: false,
    initialize: function() {
        var _this = this;
        this.initFancybox();
        _.bindAll(this, 'loadData', 'fetchSuccess', 'onScroll');
        this.collection.pager({
            error: this.fetchError, success: this.fetchSuccess,
        });

        $(document).bind('scroll', this.onScroll);
    },
    applyLayout: function() {
        $('#pins').imagesLoaded(function() {
            // Clear our previous layout handler.
            if(this.handler) this.handler.wookmarkClear();

            // Create a new layout handler.
            this.handler = $('#pins .pin');
            this.handler.wookmark({
                autoResize: true,
                offset: 3,
                itemWidth: 242
            });
        });
    },
    onScroll: function() {
        if(!this.isLoading) {
            var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100 - 500);
            if(closeToBottom) this.loadData();
        }
    },
    fetchSuccess: function(collection, response) {
        // no more pages of images to retrieve
        if(collection.currentPage == collection.totalPages) {
            // used to dont trigger loadData, if set to true
            this.noPagesLeft = true;
        }
        if(!response) {
            var noty_id = noty({
                text: 'Ett okänt fel uppstod.!',
                type: 'error'
            });
        } else {
	    _kmq.push(['record', 'Loaded page', {'Page number': collection.currentPage}]);
            this.isLoading = false;
            $('#loading-animation').hide(0);
            this.applyLayout();
        }
    },
    fetchError: function(collection, response) {
        /*var noty_id = noty({
            text: 'Inga fler bilder kunde hämtas!',
            type: 'error'
        });*/
	console.log("error");
    },
    loadData: function() {
        $('#loader').show();
        this.isLoading = true;
        this.collection.requestNextPage({error: this.fetchError, success: this.fetchSuccess, add: true });
    },
    initFancybox: function() {
        /**
         * On clicking an image show fancybox original.
         */
        $('.fancybox').fancybox({
            openEffect: 'none',
            closeEffect: 'none',
            arrows: false,
            afterShow: function() {
                if (typeof _gaq != 'undefined') {
                    // FIXME: Track which inage id
                    _kmq.push(['record', 'Image open']);
                    _gaq.push(['_trackEvent', 'Image', 'Open'])
                }

            },
        });

    },

});

Pinry.addInitializer(function(options){
    function openMainRegion() {
	Pinry.mainRegion.close();
	var PinsView1 = new PinsView({
	    collection: new PinsPagerCollection()
	});
	Pinry.mainRegion.show(PinsView1);
    }
    function trackCategory(category) {
	_kmq.push(['record', 'Changed category', {'Category': category}]);
    }

    MyRouter = Backbone.Marionette.AppRouter.extend({
        routes : {
            "klänningar" : "categoryKlanningar",
	    "*actions": "defaultRoute",
        },
        categoryKlanningar: function() {
	    global_filter = '["Midiklänningar", "Basklänningar", "Maxiklänningar", "Miniklänningar", "Klänningar", "Minikjolar", "Midikjolar"]';
	    openMainRegion();
	    trackCategory("Klanningar");
        },
	defaultRoute: function() {
	    global_filter = '[]';
	    openMainRegion();
	},
    });
    var app_router = new MyRouter();
    Backbone.history.start();
});

$(document).ready(function(){
    Pinry.start();
});
