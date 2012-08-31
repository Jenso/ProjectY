/**
 * Based on Wookmark's endless scroll.
 */
$(window).ready(function () {
    var apiURL = '/api/pin/?format=json&offset='
    var page = 0;
    var handler = null;
    var isLoading = false;
    
    /**
     * When scrolled all the way to the bottom, add more tiles.
     */
    function onScroll(event) {
      if(!isLoading) {
          var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100 + 10);
          if(closeToBottom) loadData();
      }
    };
    
    function applyLayout() {
      $('#pins').imagesLoaded(function() {
          // Clear our previous layout handler.
          if(handler) handler.wookmarkClear();
          
          // Create a new layout handler.
          handler = $('#pins .pin');
          handler.wookmark({
              autoResize: true,
              offset: 3,
              itemWidth: 242
          });
      });
    };
    
    /**
     * Loads data from the API.
     */
    function loadData() {
        isLoading = true;
        $('#loader').show();
        
        $.ajax({
            url: apiURL+(page*20),
            success: onLoadData
        });
    };
    
    /**
     * Receives data from the API, creates HTML for images and updates the layout
     */
    function onLoadData(data) {
        data = data.objects;
        isLoading = false;
        $('#loader').hide();
        
        page++;
        
        var html = '';
        var i=0, length=data.length, image;
        for(; i<length; i++) {
	          image = data[i];
	          html += '<div class="pin">';
	              /*
	              html += '<div class="pin-options">';
	                  html += '<a href="/start/delete-pin/'+image.id+'">';
	                      html += '<i class="icon-trash"></i>';
	                  html += '</a>';
	              html += '</div>';
*/
	              html += '<a class="fancybox" rel="pins" href="#'+image.id+'">';
	                  html += '<img src="'+image.url+'" width="200" >';	              
	                  html += '<strong class="PriceContainer">'
	                  html += '<p class="product-price">SEK '+image.price+'</p>';
	              html += '</strong>'
	              html += '</a>';
	              html += '<p class="product-name">'+image.name+'</p>';
	              html += '<p class="product-brand">'+image.brand+'</p>';

	          html += '</div>';
	          
	          html += '<div class="product-overlay" id="'+image.id+'">'
	          html += '<img src="'+image.url+'"/>'
	          html += '<div class="product-info">'
	          html += '<p class="overlay-name">'+image.name+'</p>';
	          html += '<p class="overlay-brand"><span>Fr&aring;n </span>'+image.brand+'</p>';
	          html += '<p class="overlay-price">'+image.price+' SEK</p>';	          
	          html += '<p class="overlay-description">'+image.real_description+'</p>';
	          html += '<a class="btn btn-warning btn-large" href="'+image.tracking_url+'">MER INFO</a>';
	          html += '<a class="btn btn-warning btn-large" href="'+image.tracking_url+'">K&Ouml;P</a>';
	          
	          html += '</div>'
	          html += '</div>'
        }
        
        
        $('#pins').append(html);
        
        applyLayout();
    };
  
    $(document).ready(new function() {
        $(document).bind('scroll', onScroll);
        loadData();
    });

    /**
     * On clicking an image show fancybox original.
     */
    $('.fancybox').fancybox({
        openEffect: 'none',
        closeEffect: 'none',
        arrows: false,
    });
});
