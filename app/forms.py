from django import forms

ACCOUNT_CHOICES = {
    0: '1年以上前のアカウント',
    1: '1年以内のアカウント',
}

class KeywordForm(forms.Form):
    keyword = forms.CharField(max_length=100, label='キーワード')
    media_count = forms.IntegerField(label='投稿数')
    followers_count = forms.IntegerField(label='フォロワー数')
    created_at = forms.ChoiceField(label='アカウント開設日', widget=forms.Select, choices=list(ACCOUNT_CHOICES.items()))
