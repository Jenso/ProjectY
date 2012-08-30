from django import forms

from .models import Pin


class PinForm(forms.ModelForm):
    url = forms.CharField(label='Picture URL', required=False)
    image = forms.ImageField(label='or Upload', required=False)
    tracking_url = forms.CharField(label='Tracking URL', required=False)
    price = forms.IntegerField(label='Price', required=False)
    name = forms.CharField(label='Name', required=False)
    brand = forms.CharField(label='Brand', required=False)
    
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = (
        	'name',
        	'brand',
            'price',
            'url',
            'image',
            'description',
            'tracking_url',
        )


    def check_if_image(self, data):
        # Test file type
        image_file_types = ['png', 'gif', 'jpeg', 'jpg']
        file_type = data.split('.')[-1]
        if file_type.lower() not in image_file_types:
            raise forms.ValidationError("Requested URL is not an image file. "
                                        "Only images are currently supported.")

    def clean(self):
        cleaned_data = super(PinForm, self).clean()

        url = cleaned_data.get('url')
        image = cleaned_data.get('image')

        if url:
            self.check_if_image(url)
            try:
                Pin.objects.get(url=url)
                raise forms.ValidationError("URL has already been pinned!")
            except Pin.DoesNotExist:
                protocol = url.split(':')[0]
                if protocol == 'http':
                    opp_url = url.replace('http://', 'https://')
                elif protocol == 'https':
                    opp_url = url.replace('https://', 'http://')
                else:
                    raise forms.ValidationError("Currently only support HTTP and "
                                                "HTTPS protocols, please be sure "
                                                "you include this in the URL.")

                try:
                    Pin.objects.get(url=opp_url)
                    raise forms.ValidationError("URL has already been pinned!")
                except Pin.DoesNotExist:
                    pass
        elif image:
            pass
        else:
            raise forms.ValidationError("Need either a URL or Upload.")

        return cleaned_data

    class Meta:
        model = Pin
        exclude = ['submitter', 'thumbnail', 'category', 'product_url']
