from django import forms

ACCOUNT_CHOICES = {
    0: 'すべてのアカウント',
    1: '最近のアカウント',
}

class KeywordForm(forms.Form):
    keyword = forms.CharField(max_length=100, label='キーワード')
    media_count = forms.IntegerField(label='投稿数')
    followers_count = forms.IntegerField(label='フォロワー数')
    created_at = forms.ChoiceField(label='アカウント開設日', widget=forms.Select, choices=list(ACCOUNT_CHOICES.items()))
    year = forms.IntegerField(label='何年前')
