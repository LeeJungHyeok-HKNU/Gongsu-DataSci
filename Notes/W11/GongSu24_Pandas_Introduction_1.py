
# coding: utf-8

# # Pandas 소개

# 앞서 살펴 보았듯이 pandas 모듈은 확률과 통계에 최적화된 파이썬 모듈이다.
# 특히, 데이터프레임(DataFrame) 자료형 클래스는 데이터 분석을 위한 다양한 기능을 제공한다.
# 데이터프레임 자료형의 기본 특성은 다음과 같다.
# 
# * 스프레드시트라고 불리는 엑셀 파일에 담긴 테이블을 모방하는 자료형이다.
# * 엑셀에서 제공하는 다양한 기능을 기본 함수(메소드)로 제공한다.
# * 인덱싱, 슬라이싱 기능은 넘파이 모듈의 2차원 어레이와 기본적으로 유사하게 작동한다.
# * SQL이 데이터베이스를 다루는 기능과 유사한 기능 제공

# #### pandas 기초 자료 안내
# 
# pandas의 기초적인 활용에 대해서는 아래 두 사이트를 언급하는 것으로 하고 넘어간다.
# 강의 시간에 일부 내용을 함께 확인할 예정이다.
# 
# 먼저 아래 사이트의 내용 중 5.2절까지의 내용을 먼저 본다.
# 
# * http://sinpong.tistory.com/category/Python%20for%20data%20analysis
# 
# 그 후에 아래 사이트 내용을 한 번 훑어 본다.
# 
# * http://ourcstory.tistory.com/145
# 
# 위 사이트의 소스코드는 아래 사이트를 참조하면 쉽게 얻을 수 있다.
# 
# https://github.com/liganega/10-minutes-to-pandas/blob/master/notebooks/10-minutes-to-pandas.ipynb
# 
# 이제 다시 아내 사이트의 내용 중 5.2절 이후를 살펴본다.
# 
# 강의노트로 돌아와서 GongSu21 장 내용을 다시 한 번 살펴본다.

# #### 안내
# 
# 아래 내용은 다음 사이트를 참조하여 작성하였음.
# 
# http://sinpong.tistory.com/category/Python%20for%20data%20analysis
# 
# 

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# pd는 pandas를 지칭하며 Series와 DataFrame은 원래 pandas 모듈에서 정의된 함수들이어서 기본적으로 
# pd.Series() 또는 pd.DataFrame() 형식으로 호출해야 한다.
# 하지만 많이 사용되는 함수들이기에 두 함수를 따로 임포트 하면 `"pd."` 부분은 생략이 가능하다.
# 즉, 로컬 네임스페이스로 import하는 것이 편해서 이렇게 사용한다.

# pandas에 대해서 알아보려면 Series와 DataFrame, 이 두 가지 자료 구조에 익숙해져야 한다.

# ## 시리즈(Series) 자료형
# 
# Series는 넘파이의 1차원 어레이와 비슷한 자료형이다. 각각의 항목은 임의의, 하지만 동일한 자료형을 가져야 한다. 
# 어레이와 다른 점은 사용자가 지정할 수 있는 색인들의 목록인 index가 항상 함께 사용된다는 점이다. 

# ### 시리즈 생성: 어레이 및 리스트 활용
# 
# 시리즈를 다양한 방식으로 생성할 수 있다.
# 먼저 어레이 및 리스트 활용하여 시리즈를 생성하는 것을 살펴 본다.

# In[2]:

ser1 = Series([4, -7, -5, 3])
ser1


# index를 지정하지 않으면 어레이 인덱싱에서 사용되는 숫자가 자동으로 사용된다.
# 
# * 색인은 0부터 시작한다. 

# ### 값(values)과 인덱스(index) 속성
# 
# 시리즈(Series)는 값들의 어레이와 색인들의 목록으로 구성되며, 각각을 values와 index 속성을 통해 확인할 수 있다.

# In[3]:

ser1.values


# In[4]:

ser1.index


# #### index 지정
# 
# 색인들의 목록을 사용자가 임의로 지정하면서 시리즈를 생성할 수 있다.

# In[5]:

ser2 = Series([4, -7, -5, 3], index=['a', 'b', 'c', 'd'])
ser2


# index를 확인하면 기본 인덱스와 다른 자료형이 사용되었음을 확인할 수 있다.

# In[6]:

ser2.index


# 색인은 대입을 통해서도 변경할 수 있다.

# In[7]:

ser2.index = ['A', 'B', 'C', 'D']
ser2


# #### 인덱싱
# 
# 시리즈 인덱싱은 기본적으로 어레이 인덱싱과 비슷하다.

# In[8]:

ser2['C']


# 여러 개의 색인을 활용하여 인덱싱을 하면 시리즈 값이 리턴된다.
# 
# * 리스트를 색인들의 목록으로 활용한다.
# * 사용된 색인 순서에 맞추어 시리즈가 결정된다.

# In[9]:

ser3 = ser2[['D', 'A', 'B']]
ser3


# #### 마스크 인덱싱
# 
# 넘파이 어레이에서의 마스크 인덱싱 기능을 거의 동일하게 활용할 수 있다.

# In[10]:

mask = ser2 > 0
mask


# In[11]:

ser2[mask]


# ### 시리즈 연산
# 
# 시리즈 연산은 어레이의 연산과 동일하다.
# 
# * 기본적으로 항목별로 연산이 작동한다.
# * index 는 기본적으로 변하지 않는다.
# * 두 시리즈의 합은 인덱스의 존재 여부에 많은 영향을 받는다.

# In[12]:

ser2 * 2


# In[13]:

def f(x):
    return x/2 + 1/2


# In[14]:

f(ser2)


# #### 특정 색인 사용 여부 판단
# 
# `in` 연산자를 활용하여 특정 색인의 사용여부를 판단할 수 있다.

# In[15]:

'B' in ser2


# In[16]:

'one' in ser2


# ### 시리즈 생성: 사전 활용

# 시리즈 자료형은 사전 자료형과 매우 비슷하다. 다만 values에 동일한 자료형이 사용되어야 한다는 점에 다르다.
# 따라서 사전 자료형을 이용하여 시리즈를 쉽게 생성할 수 있다.

# In[17]:

dic1 = {'Oh':2300, 'Ts': 1700, 'Or':1600, 'Ah':4500}
ser4  = Series(dic1)
ser4


# 새로운 index를 사용할 경우, 기존의 사전에 사용되지 않은 key에는 값이 누락되었다는 의미로 NaN이 사용된다.
# 
# **주의:** NaN은 Not a Number의 줄임말로 어떤 값도 할당되지 않았음, 즉 널(Null)임을 의미한다. 

# In[18]:

keys1 = ['Ca', 'Oh', 'Or', 'Ts', 'Gg']
ser5 = Series(dic1, index=keys1)
ser5


# #### 널(null) 값 확인 함수
# 
# `isnull`과 `notnull` 함수는 누락된 데이터의 위치를 확인할 때 사용한다.
# 
# 두 함수 모두 시리즈 자료형을 리턴한다.

# In[19]:

pd.isnull(ser5)


# In[20]:

pd.notnull(ser5)


# ### 시리즈의 합
# 
# 시리즈의 연산은 동일한 색인에 대해서만 기본적으로 값의 합이 이루어진다. 
# 아래의 경우는 널값이 사용된다.
# * 두 시리즈에서 동시에 사용된 색인이 아닌 경우
# * 두 시리즈에서 동시에 색인으로 사용되었지만 최소 하나의 경우에서 널값을 갖는 경우

# In[21]:

ser4


# In[22]:

ser5


# In[23]:

ser4 + ser5


# ### name 속성
# 
# name 속성을 이용하여 Series와 index에 이름을 지정할 수 있다.

# #### Series 의 name 속성 설정

# In[24]:

ser5.name = 'Population'


# #### index 의 name 속성 설정

# In[25]:

ser5.index.name = 'State'


# 이제 ser5의 name 속성과 ser5.index의 속성이 설정되었음을 아래와 같이 확인할 수 있다.

# In[26]:

ser5


# ## 데이터프레임(DataFrame) 자료형
# 
# 데이터프레임 자료형은 동일한 색인 목록(index)을 공유하는 여러 개의 시리즈를 붙혀 놓은 자료형으로 생각할 수 있다.
# 내부적으로는 행렬 모양의 2차원 어레이로 취급된다. 
# 
# 앞서 다룬 Weed_Price.csv 파일을 읽어 드렸을 때 사용되는 모습을 생각하면 여러 개의 Series를 붙혀놓은 모습이 데이터프레임이라는 것을 쉽게 이해할 수 있다.

# In[27]:

weed_pd = pd.read_csv("data/Weed_Price.csv", parse_dates=[-1])
weed_pd.head()


# weed_pd에 할당된 데이터프레임에는 총 8개의 Series가 사용되었다.
# 각각의 시리즈의 이름(name)은 다음과 같다.
#     
#     State, HighQ, HighQN, MedQ, MedQN, LowQ, LowQN, date
#     
# 또한 언급된 8개의 시리즈의 index는 모두 기본 index를 사용하고 있다.

# ### 데이터프레임 생성: 사전 활용
# 
# 아래의 경우처럼 키값이 동일한 길이의 리스트 또는 어레이인 사전을 활용하여 DataFrame을 생성할 수 있다.

# In[28]:

data = {'state' : ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],        'year' : [2000, 2001, 2002, 2001, 2002],        'pop' : [1.5, 1.7, 3.6, 2.4, 2.9]}


# In[29]:

dframe = DataFrame(data)
dframe


# 사전 자료형을 이용하였기 때문에 시리즈의 순서가 임의로 지정되었다. 
# 특정 순서로 시리즈를 나열하려면 columns 키워드 인자를 이용해야 한다.

# In[30]:

DataFrame(data, columns=['year', 'state', 'pop'])


# Series의 경우처럼 index를 지정할 수 있다.

# In[31]:

dframe2 = DataFrame(data, index=['one','two','three','four','five'])
dframe2


# ### 데이터프레임 생성: 데이터프레임 활용
# 
# 기존의 데이터프레임을 활용하여 새로운 데이터프레임을 생성할 수 있다.

# In[32]:

dframe3 = DataFrame(dframe2)
dframe3


# 아래 코드는 기존의 데이터프레임에 컬럼을 확장하는 방식으로 새로운 데이터프레임을 생성한다.
# 
# **주의:** 새 컬럼에 값을 지정하지 않으므로 널값이 할당된다.

# In[33]:

dframe4 = DataFrame(dframe3, columns=['year', 'state', 'pop', 'debt'])
dframe4


# 컬럼의 이름의 목록은 columns 속성에 저장되어 있다.

# In[34]:

dframe4.columns


# ### 칼럼별 인덱싱
# 
# * 컬럼의 이름을 키로 사용하여 인덱싱을 한다.

# In[35]:

dframe4['year']


# 각각의 컬럼이 Series 자료형임을 확인할 수 있다.

# In[36]:

type(dframe4['year'])


# * 각각의 컬럼의 이름(name)이 속성으로 지정되어 있기 때문에 속성으로 확인할 수도 있다.

# In[37]:

dframe4.year


# #### 컬럼 값 지정하기
# 
# 컬럼 인덱싱을 사용하여 값을 지정할 수 있다.
# 아래 코드는 debt 컬럼에 일정한 값을 지정할 때 사용한다.

# In[38]:

dframe4['debt'] = 16.5
dframe4


# 아래 코드는 index의 길이와 동일한 크기의 어레이나 리스트를 활용하는 방법이다.

# In[39]:

dframe4['debt'] = np.arange(5.)
dframe4


# **주의:** 정수 5 대신에 부동소수점 5.를 사용하는 이유는 debt 컬럼의 자료형을 float로 설정하기 위함이다.

# In[40]:

dframe4.dtypes


# 특정 컬럼의 데이터를 Series를 이용하여 지정할 때는 DataFrame의 색인에 따라 값이 대입되며 없는 색인에는 값이 대입되지 않는다.

# In[41]:

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
val


# In[42]:

dframe4['debt'] = val
dframe4


# ### 행별 인덱싱
# 
# * 행별 인덱싱은 색인 이름 또는 0, 1, 2, 등의 기본 색인을 이용한다.

# #### 색인 이름 인덱싱
# 
# * loc 메소드 활용
# * loc은 location(위치)의 줄임말이다.

# In[43]:

dframe4.loc['three']


# loc의 리턴값은 시리즈이다. 

# In[44]:

type(dframe4.loc['three'])


# 컬럼의 이름이 index로 사용되었음에 주의한다.

# In[45]:

dframe4.loc['three'].index


# #### 행별 값 지정
# 
# 컬럼의 개수와 컬럼별 자료형과 동일한 값들을 사용하는 리스트를 활용하여 행별 값을 설정할 수 있다.

# In[46]:

dframe4.loc['three'] = [2017, 'GG', 2.3, 3.0]
dframe4


# ### 컬럼 추가
# 
# 없는 칼럼을 대입하면 새로운 칼럼이 생성된다. 
# 
# 참고: eastern은 부활절을 의미한다.

# In[47]:

dframe4['eastern']= (dframe4.state == 'Ohio')
dframe4


# 참고: `state == 'ohio'`는 시리즈를 생성한다.

# In[48]:

dframe4.state == 'Ohio'


# ### 컬럼 삭제
# 
# 파이썬 사전형에서와 마찬가지로 del 함수를 사용해서 칼럼을 삭제할 수 있다.

# In[49]:

del dframe4['eastern']
dframe4


# ### 인덱싱과 뷰 방식

# DataFrame의 색인을 이용해서 생성된 칼럼은 내부 데이터에 대한 뷰(view)이며 복사가 이루어지지 않는다. 
# 따라서 이렇게 얻은 Series 객체에 대한 변경은 실제 DataFrame에 반영된다. 
# 복사본이 필요할 때는 Series의 copy 메서드를 이용하자.

# In[50]:

dframe4


# In[51]:

debt_col = dframe4.debt
debt_col


# 아래와 같이 인덱싱을 사용하여 값을 변경할 수는 있지만 경고문이 뜬다.
# 경고문은 슬라이싱(인덱싱) 결과에 수정을 가할 때 조심해야 한다는 내용이다. 

# In[72]:

debt_col.loc['one'] = 1.2


# 하지만 값이 기존의 dframe4까지 영향을 주는 것을 아래와 같이 확인할 수 있다.
# 위 경고문의 내용처럼 뷰 방식으로 작동하는 경우 데이터를 수정할 때 매우 조심해야 한다.

# In[53]:

dframe4


# `copy()` 메소드를 사용하면 앞서 설명한 문제는 발생하지 않는다. 

# In[54]:

debt_col_copy = dframe4.debt.copy()


# `debt_col_copy`의 데이터를 수정하자. 
# 더 이상 경고문이 뜨지 않는다.

# In[55]:

debt_col_copy.loc['one'] = -1.2


# 또한 기존의 `dframe4`가 변경되지 않았음을 확인할 수 있다.

# In[57]:

dframe4


# ### 데이터프레임 생성: 중첩 사전 활용
# 
# * 중첩 사전을 이용하여 데이터플레임을 생성할 수 있다.

# In[58]:

pop = {'Nevada' : {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}


# 바깥에 있는 사전의 키 값이 칼럼이 되고 안에 있는 키는 인덱스가 된다.

# In[59]:

dframe5 = DataFrame(pop)
dframe5


# * 색인을 직접 지정한다면 지정된 색인으로 DataFrame을 생성한다.

# In[60]:

DataFrame(pop, index=[2001, 2002, 2003])


# * Series 객체를 담고 있는 사전 데이터도 같은 방식으로 취급된다.

# In[61]:

dframe5['Ohio'][:-1]


# In[62]:

dframe5['Nevada'][:2]


# In[63]:

pdata = {'ohio' : dframe5['Ohio'][:-1],
         'Nevada': dframe5['Nevada'][:2]}
DataFrame(pdata)


# ### 전치행렬 활용
# 
# 넘파이에서와 마찬가지로 행과 열을 바꿀 수 있다.

# #### 주의
# 
# 전치행렬이 뷰 방식을 따른다. 
# 따라서 기본적으로 copy() 함수를 사용하여 기존 데이터와의 관계를 끊는 게 좋다.

# In[64]:

dframe5T = dframe5.T.copy()
dframe5T


# In[65]:

dframe5['Nevada'].iloc[0] = 1.0
dframe5


# In[66]:

dframe5T


# ### name 속성
# 
# name 속성을 이용하여 컬럼과 index에 이름을 지정할 수 있다.

# In[68]:

dframe5.index.name = 'year'
dframe5.columns.name = 'state'
dframe5


# ### 값(values) 속성
# 
# Series와 유사하게 values 속성은 DataFrame에 저장된 데이터를 2차원 배열로 반환한다.

# In[69]:

dframe5.values


# DataFrame의 칼럼에 서로 다른 dtype이 있다면 모든 칼럼을 수용하기 위해 object라는 dtype이 선택된다.
# object를 만능 자료형이라 생각하면 편하다. 실제로는 4개의 포인터로 구성된다.

# In[70]:

dframe3.values

