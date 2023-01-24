#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
from shroomdk import ShroomDK
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.ticker as ticker
import numpy as np
import plotly.express as px
sdk = ShroomDK("7bfe27b2-e726-4d8d-b519-03abc6447728")
st.cache(suppress_st_warning=True)
st.set_page_config(page_title="Near Developer Activity", layout="wide",initial_sidebar_state="collapsed")
st.title('Near Developer Activity')



# In[20]:


st.markdown('NEAR Protocol is a proof-of-stake public blockchain with smart contract capability that aims to act as a community-managed cloud computing platform.  It provides a platform on which developers can build decentralized applications (dapps).')

st.markdown('With Electric Capital’s release of its annual report on developer activity, the topic of “developers” is a hot topic across crypto and NEAR has been one of the blockchains to consider because of its important growth since its inception.')

st.markdown('One of the main aspects to consider for these type of L1 blockchains is the competence. Users are constantly choosing for the best network to act and to use considering several aspects such as speed, success transactions, performance etc. But which developers are behind the protocol is also a very important thing to take into account.')


# In[5]:


st.markdown('For this reason, the intention of this analysis is to provide information about the current status of Near Protocol developer activity by providing metrics such as:') 
st.write('- Active developers')
st.write('- New developers')
st.write('- Type of developers')
st.write('- Development activity vs NEAR price')
st.write('- Developer retention evolution')
st.write('')


# In[10]:

sql0 = f"""
SELECT
  count(distinct author) as total_developers,
count(distinct id) as total_pulls,
  count(distinct repo) as total_repositories
from near.beta.github_activity
"""

sql00 = f"""
SELECT
  count(distinct author) as total_developers,
count(distinct id) as total_pulls,
  count(distinct repo) as total_repositories
from near.beta.github_activity where updatedat between '2022-01-01' and '2023-01-01'
"""

sql000 = f"""
SELECT
  count(distinct author) as total_developers,
count(distinct id) as total_pulls,
  count(distinct repo) as total_repositories
from near.beta.github_activity where updatedat >= '2023-01-01'
"""

sql = f"""
SELECT
  trunc(updatedat,'day') as date,
  count(distinct author) as developers,
  sum(developers) over (order by date) as cum_developers,
count(distinct id) as pulls,
  sum(pulls) over (order by date) as cum_pulls,
  count(distinct repo) as repositories,
  sum(repositories) over (order by date) as cum_repositories
from near.beta.github_activity where date>=CURRENT_DATE-INTERVAL '1 MONTH'
  group by 1
order by 1 asc 
"""

sql2 = f"""
SELECT
  trunc(updatedat,'week') as date,
  count(distinct author) as developers,
  sum(developers) over (order by date) as cum_developers,
count(distinct id) as pulls,
  sum(pulls) over (order by date) as cum_pulls,
  count(distinct repo) as repositories,
  sum(repositories) over (order by date) as cum_repositories
from near.beta.github_activity where date>=CURRENT_DATE-INTERVAL '3 MONTHS'
  group by 1
order by 1 asc 


"""

sql3 = f"""
SELECT
  trunc(updatedat,'month') as date,
  count(distinct author) as developers,
  sum(developers) over (order by date) as cum_developers,
count(distinct id) as pulls,
  sum(pulls) over (order by date) as cum_pulls,
  count(distinct repo) as repositories,
  sum(repositories) over (order by date) as cum_repositories
from near.beta.github_activity 
  group by 1
order by 1 asc 

"""

sql4="""
with news as (
  SELECT
  distinct author,
  min(trunc(createdat,'day')) as debut
  from near.beta.github_activity
  group by 1
  )
  SELECT
  debut,
  count(distinct author) as new_developers,
  sum(new_developers) over (order by debut) as cum_new_developers
from news where debut>=CURRENT_DATE-INTERVAL '1 MONTH'
  group by 1
order by 1 asc 

"""

sql5="""
with news as (
  SELECT
  distinct author,
  min(trunc(createdat,'week')) as debut
  from near.beta.github_activity
  group by 1
  )
  SELECT
  debut,
  count(distinct author) as new_developers,
  sum(new_developers) over (order by debut) as cum_new_developers
from news where debut>=CURRENT_DATE-INTERVAL '3 MONTHS'
  group by 1
order by 1 asc 

"""

sql6="""
with news as (
  SELECT
  distinct author,
  min(trunc(createdat,'month')) as debut
  from near.beta.github_activity
  group by 1
  )
  SELECT
  debut,
  count(distinct author) as new_developers,
  sum(new_developers) over (order by debut) as cum_new_developers
from news
  group by 1
order by 1 asc 

"""

sql7="""
with news as (
  SELECT
  distinct id as pulls,
  min(trunc(createdat,'day')) as debut
  from near.beta.github_activity
  group by 1
  )
  SELECT
  debut,
  count(distinct pulls) as new_pulls,
  sum(new_pulls) over (order by debut) as cum_new_pulls
from news where debut>=CURRENT_DATE-INTERVAL '3 MONTHS'
  group by 1
order by 1 asc 

"""

sql8="""
with news as (
  SELECT
  distinct id as pulls,
  min(trunc(createdat,'week')) as debut
  from near.beta.github_activity
  group by 1
  )
  SELECT
  debut,
  count(distinct pulls) as new_pulls,
  sum(new_pulls) over (order by debut) as cum_new_pulls
from news where debut>=CURRENT_DATE-INTERVAL '3 MONTHS'
  group by 1
order by 1 asc 

"""

sql9="""
with news as (
  SELECT
  distinct id as pulls,
  min(trunc(createdat,'month')) as debut
  from near.beta.github_activity
  group by 1
  )
  SELECT
  debut,
  count(distinct pulls) as new_pulls,
  sum(new_pulls) over (order by debut) as cum_new_pulls
from news
  group by 1
order by 1 asc 

"""

sql10="""
with news as (
  SELECT
  distinct repo as repositories,
  min(trunc(createdat,'day')) as debut
  from near.beta.github_activity
  group by 1
  )
  SELECT
  debut,
  count(distinct repositories) as new_repositories,
  sum(new_repositories) over (order by debut) as cum_new_repositories
from news where debut>=CURRENT_DATE-INTERVAL '3 MONTHS'
  group by 1
order by 1 asc 

"""
sql11="""
with news as (
  SELECT
  distinct repo as repositories,
  min(trunc(createdat,'week')) as debut
  from near.beta.github_activity
  group by 1
  )
  SELECT
  debut,
  count(distinct repositories) as new_repositories,
  sum(new_repositories) over (order by debut) as cum_new_repositories
from news where debut>=CURRENT_DATE-INTERVAL '3 MONTHS'
  group by 1
order by 1 asc 
"""
sql12="""
with news as (
  SELECT
  distinct id as repositories,
  min(trunc(createdat,'month')) as debut
  from near.beta.github_activity
  group by 1
  )
  SELECT
  debut,
  count(distinct repositories) as new_repositories,
  sum(new_repositories) over (order by debut) as cum_new_repositories
from news
  group by 1
order by 1 asc 

"""


# In[11]:


st.experimental_memo(ttl=21600)
@st.cache
def compute(a):
    results=sdk.query(a)
    return results

results0 = compute(sql0)
df0 = pd.DataFrame(results0.records)
df0.info()

results00 = compute(sql00)
df00 = pd.DataFrame(results00.records)
df00.info()

results000 = compute(sql000)
df000 = pd.DataFrame(results000.records)
df000.info()

results = compute(sql)
df = pd.DataFrame(results.records)
df.info()

results2 = compute(sql2)
df2 = pd.DataFrame(results2.records)
df2.info()

results3 = compute(sql3)
df3 = pd.DataFrame(results3.records)
df3.info()

results4 = compute(sql4)
df4 = pd.DataFrame(results4.records)
df4.info()

results5 = compute(sql5)
df5 = pd.DataFrame(results5.records)
df5.info()

results6 = compute(sql6)
df6 = pd.DataFrame(results6.records)
df6.info()

results7 = compute(sql7)
df7 = pd.DataFrame(results7.records)
df7.info()

results8 = compute(sql8)
df8 = pd.DataFrame(results8.records)
df8.info()

results9 = compute(sql9)
df9 = pd.DataFrame(results9.records)
df9.info()

results10 = compute(sql10)
df10 = pd.DataFrame(results10.records)
df10.info()

results11 = compute(sql11)
df11 = pd.DataFrame(results11.records)
df11.info()

results12 = compute(sql12)
df12 = pd.DataFrame(results12.records)
df12.info()

# In[22]:

st.subheader('New and active developer activity')
st.write('The first metrics to be analyzed are the new and active developers as well as its activity over the past days,weeks and months.')
st.write('In concrete, the following charts shows:')
st.write('- Last month active and new developers (daily and cumulative)')
st.write('- Last 3 months active and new developers (weekly and cumulative)')
st.write('- Active and new developers over time (monthly and cumulative)')
st.write('- Last month total and new repositories and pull requests (daily and cumulative)')
st.write('- Last 3 months total and new repositories and pull requests (weekly and cumulative)')
st.write('- Total and new repositories and pull requests over time (monthly and cumulative)')
st.write('')

import math

millnames = ['',' k',' M',' B',' T']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])


# In[43]:


st.markdown(""" <style> div.css-12w0qpk.e1tzin5v2{
 background-color: #f5f5f5;
 border: 2px solid;
 padding: 10px 5px 5px 5px;
 border-radius: 10px;
 color: #ffc300;
 box-shadow: 10px;
}
div.css-1r6slb0.e1tzin5v2{
 background-color: #f5f5f5;
 border: 2px solid; /* #900c3f */
 border-radius: 10px;
 padding: 10px 5px 5px 5px;
 color: green;
}
div.css-50ug3q.e16fv1kl3{
 font-weight: 900;
} 
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> div.css-ocqkz7.e1tzin5v4{
 background-color: #f5f5f5;
 border: 2px solid;
 padding: 10px 5px 5px 5px;
 border-radius: 10px;
 color: #ffc300;
 box-shadow: 10px;
}
div.css-keje6w.ce1tzin5v2{
 background-color: #f5f5f5;
 border: 2px solid; /* #900c3f */
 border-radius: 10px;
 padding: 10px 5px 5px 5px;
 color: orange;
}
div.css-12ukr4l.e1tzin5v0{
 font-weight: 900;
} 
</style> """, unsafe_allow_html=True)

col1,col2,col3 =st.columns(3)
with col1:
    st.metric('Total Near developers', millify(df0['total_developers'][0]))
col2.metric('Active developers in 2022', millify(df00['total_developers'][0]))
col3.metric('Active developers in 2023', millify(df000['total_developers'][0]))

col1,col2,col3 =st.columns(3)
with col1:
    st.metric('Total Near repositories', millify(df0['total_repositories'][0]))
col2.metric('Active repositories in 2022', millify(df00['total_repositories'][0]))
col3.metric('Active repositories in 2023', millify(df000['total_repositories'][0]))

col1,col2,col3 =st.columns(3)
with col1:
    st.metric('Total Near pull requests', millify(df0['total_pulls'][0]))
col2.metric('Active pull requests in 2022', millify(df00['total_pulls'][0]))
col3.metric('Active pull requests in 2023', millify(df000['total_pulls'][0]))

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['date'],
                y=df['developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig1.add_trace(go.Line(x=df['date'],
                y=df['cum_developers'],
                name='# of users',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig1.update_layout(
    title='Active developers',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig1.update_yaxes(title_text="Daily active developers", secondary_y=False)
fig1.update_yaxes(title_text="Total active developers", secondary_y=True)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df2['date'],
                y=df2['developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df2['date'],
                y=df2['cum_developers'],
                name='# of users',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Active developers',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig2.update_yaxes(title_text="Weekly active developers", secondary_y=False)
fig2.update_yaxes(title_text="Total active developers", secondary_y=True)


# Create figure with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Bar(x=df3['date'],
                y=df3['developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig3.add_trace(go.Line(x=df3['date'],
                y=df3['cum_developers'],
                name='# of users',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig3.update_layout(
    title='Active developers',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig3.update_yaxes(title_text="Monthly active developers", secondary_y=False)
fig3.update_yaxes(title_text="Total active developers", secondary_y=True)

tab1, tab2, tab3 = st.tabs(["Daily developers", "Weekly developers", "Monthly developers"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)


# Create figure with secondary y-axis
fig4 = make_subplots(specs=[[{"secondary_y": True}]])

fig4.add_trace(go.Bar(x=df4['debut'],
                y=df4['new_developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig4.add_trace(go.Line(x=df4['debut'],
                y=df4['cum_new_developers'],
                name='# of users',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig4.update_layout(
    title='New Near developers',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig4.update_yaxes(title_text="Daily new Near developers", secondary_y=False)
fig4.update_yaxes(title_text="Total new Near developers", secondary_y=True)

# Create figure with secondary y-axis
fig5 = make_subplots(specs=[[{"secondary_y": True}]])

fig5.add_trace(go.Bar(x=df5['debut'],
                y=df5['new_developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig5.add_trace(go.Line(x=df5['debut'],
                y=df5['cum_new_developers'],
                name='# of users',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig5.update_layout(
    title='New Near developers',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig5.update_yaxes(title_text="Weekly Near developers", secondary_y=False)
fig5.update_yaxes(title_text="Total weekly Near developers", secondary_y=True)


# Create figure with secondary y-axis
fig6 = make_subplots(specs=[[{"secondary_y": True}]])

fig6.add_trace(go.Bar(x=df6['debut'],
                y=df6['new_developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig6.add_trace(go.Line(x=df6['debut'],
                y=df6['cum_new_developers'],
                name='# of users',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig6.update_layout(
    title='New Near developers',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig6.update_yaxes(title_text="Monthly new Near developers", secondary_y=False)
fig6.update_yaxes(title_text="Total new Near developers", secondary_y=True)

tab1, tab2, tab3 = st.tabs(["Daily new developers", "Weekly new developers", "Monthly new developers"])

with tab1:
    st.plotly_chart(fig4, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig5, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig6, theme="streamlit", use_container_width=True)
    
    
    
 # Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['date'],
                y=df['repositories'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig1.add_trace(go.Line(x=df['date'],
                y=df['cum_repositories'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig1.update_layout(
    title='Active repositories',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig1.update_yaxes(title_text="Daily active repositories", secondary_y=False)
fig1.update_yaxes(title_text="Total active repositories", secondary_y=True)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df2['date'],
                y=df2['repositories'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df2['date'],
                y=df2['cum_repositories'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Active repositories',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig2.update_yaxes(title_text="Weekly active repositories", secondary_y=False)
fig2.update_yaxes(title_text="Total active repositories", secondary_y=True)


# Create figure with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Bar(x=df3['date'],
                y=df3['repositories'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig3.add_trace(go.Line(x=df3['date'],
                y=df3['cum_repositories'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig3.update_layout(
    title='Active repositories',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig3.update_yaxes(title_text="Monthly active repositories", secondary_y=False)
fig3.update_yaxes(title_text="Total active repositories", secondary_y=True)

tab1, tab2, tab3 = st.tabs(["Daily repositories", "Weekly repositories", "Monthly repositories"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)


# Create figure with secondary y-axis
fig4 = make_subplots(specs=[[{"secondary_y": True}]])

fig4.add_trace(go.Bar(x=df10['debut'],
                y=df10['new_repositories'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig4.add_trace(go.Line(x=df10['debut'],
                y=df10['cum_new_repositories'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig4.update_layout(
    title='New Near repositories',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig4.update_yaxes(title_text="Daily new Near repositories", secondary_y=False)
fig4.update_yaxes(title_text="Total new Near repositories", secondary_y=True)

# Create figure with secondary y-axis
fig5 = make_subplots(specs=[[{"secondary_y": True}]])

fig5.add_trace(go.Bar(x=df11['debut'],
                y=df11['new_repositories'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig5.add_trace(go.Line(x=df11['debut'],
                y=df11['cum_new_repositories'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig5.update_layout(
    title='New Near repositories',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig5.update_yaxes(title_text="Weekly Near repositories", secondary_y=False)
fig5.update_yaxes(title_text="Total weekly Near repositories", secondary_y=True)


# Create figure with secondary y-axis
fig6 = make_subplots(specs=[[{"secondary_y": True}]])

fig6.add_trace(go.Bar(x=df12['debut'],
                y=df12['new_repositories'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig6.add_trace(go.Line(x=df12['debut'],
                y=df12['cum_new_repositories'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig6.update_layout(
    title='New Near repositories',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig6.update_yaxes(title_text="Monthly new Near repositories", secondary_y=False)
fig6.update_yaxes(title_text="Total new Near repositories", secondary_y=True)

tab1, tab2, tab3 = st.tabs(["Daily new repositories", "Weekly new repositories", "Monthly new repositories"])

with tab1:
    st.plotly_chart(fig4, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig5, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig6, theme="streamlit", use_container_width=True)

    

    
# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['date'],
                y=df['pulls'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig1.add_trace(go.Line(x=df['date'],
                y=df['cum_pulls'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig1.update_layout(
    title='Active pulls',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig1.update_yaxes(title_text="Daily active pulls", secondary_y=False)
fig1.update_yaxes(title_text="Total active pulls", secondary_y=True)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df2['date'],
                y=df2['pulls'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df2['date'],
                y=df2['cum_pulls'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Active pulls',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig2.update_yaxes(title_text="Weekly active pulls", secondary_y=False)
fig2.update_yaxes(title_text="Total active pulls", secondary_y=True)


# Create figure with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Bar(x=df3['date'],
                y=df3['pulls'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig3.add_trace(go.Line(x=df3['date'],
                y=df3['cum_pulls'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig3.update_layout(
    title='Active pulls',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig3.update_yaxes(title_text="Monthly active pulls", secondary_y=False)
fig3.update_yaxes(title_text="Total active pulls", secondary_y=True)

tab1, tab2, tab3 = st.tabs(["Daily pulls", "Weekly pulls", "Monthly pulls"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)


# Create figure with secondary y-axis
fig4 = make_subplots(specs=[[{"secondary_y": True}]])

fig4.add_trace(go.Bar(x=df7['debut'],
                y=df7['new_pulls'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig4.add_trace(go.Line(x=df7['debut'],
                y=df7['cum_new_pulls'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig4.update_layout(
    title='New Near pulls',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig4.update_yaxes(title_text="Daily new Near pulls", secondary_y=False)
fig4.update_yaxes(title_text="Total new Near pulls", secondary_y=True)

# Create figure with secondary y-axis
fig5 = make_subplots(specs=[[{"secondary_y": True}]])

fig5.add_trace(go.Bar(x=df8['debut'],
                y=df8['new_pulls'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig5.add_trace(go.Line(x=df8['debut'],
                y=df8['cum_new_pulls'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig5.update_layout(
    title='New Near pulls',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig5.update_yaxes(title_text="Weekly Near pulls", secondary_y=False)
fig5.update_yaxes(title_text="Total weekly Near pulls", secondary_y=True)


# Create figure with secondary y-axis
fig6 = make_subplots(specs=[[{"secondary_y": True}]])

fig6.add_trace(go.Bar(x=df9['debut'],
                y=df9['new_pulls'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig6.add_trace(go.Line(x=df9['debut'],
                y=df9['cum_new_pulls'],
                name='# of repos',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig6.update_layout(
    title='New Near pulls',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig6.update_yaxes(title_text="Monthly new Near pulls", secondary_y=False)
fig6.update_yaxes(title_text="Total new Near pulls", secondary_y=True)

tab1, tab2, tab3 = st.tabs(["Daily new pulls", "Weekly new pulls", "Monthly new pulls"])

with tab1:
    st.plotly_chart(fig4, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig5, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig6, theme="streamlit", use_container_width=True)    
    
    
    
    
    
sql0="""
SELECT
  AUTHORASSOCIATION as type,
  count(distinct author) as total_developers
from near.beta.github_activity --where updatedat between '2022-01-01' and '2023-01-01'
group by 1
"""

sql00="""
SELECT
  AUTHORASSOCIATION as type,
  count(distinct author) as total_developers
from near.beta.github_activity where updatedat between '2022-01-01' and '2023-01-01'
group by 1
"""

sql000="""
SELECT
  AUTHORASSOCIATION as type,
  count(distinct author) as total_developers
from near.beta.github_activity where updatedat >= '2023-01-01'
group by 1
"""


sql = f"""
SELECT
  trunc(updatedat,'day') as date,
  AUTHORASSOCIATION as type,
  count(distinct author) as developers,
  sum(developers) over (order by date) as cum_developers
from near.beta.github_activity where date>=CURRENT_DATE-INTERVAL '1 MONTH'
  group by 1,2
order by 1 asc 
"""

sql2 = f"""
SELECT
  trunc(updatedat,'week') as date,
  AUTHORASSOCIATION as type,
  count(distinct author) as developers,
  sum(developers) over (order by date) as cum_developers
from near.beta.github_activity where date>=CURRENT_DATE-INTERVAL '3 MONTHS'
  group by 1,2
order by 1 asc 

"""

sql3 = f"""
SELECT
  trunc(updatedat,'month') as date,
  AUTHORASSOCIATION as type,
  count(distinct author) as developers,
  sum(developers) over (order by date) as cum_developers
from near.beta.github_activity 
  group by 1,2
order by 1 asc 

"""



sql4="""
with news as (
  SELECT
  distinct author,
  AUTHORASSOCIATION as type,
  min(trunc(createdat,'day')) as debut
  from near.beta.github_activity
  group by 1,2
  )
  SELECT
  debut,type,
  count(distinct author) as new_developers,
  sum(new_developers) over (partition by type order by debut) as cum_new_developers
from news where debut>=CURRENT_DATE-INTERVAL '1 MONTH'
  group by 1,2
order by 1 asc 

"""

sql5="""
with news as (
  SELECT
  distinct author,AUTHORASSOCIATION as type,
  min(trunc(createdat,'week')) as debut
  from near.beta.github_activity
  group by 1,2
  )
  SELECT
  debut,type,
  count(distinct author) as new_developers,
  sum(new_developers) over (partition by type order by debut) as cum_new_developers
from news where debut>=CURRENT_DATE-INTERVAL '3 MONTHS'
  group by 1,2
order by 1 asc 

"""

sql6="""
with news as (
  SELECT
  distinct author,AUTHORASSOCIATION as type,
  min(trunc(createdat,'month')) as debut
  from near.beta.github_activity
  group by 1,2
  )
  SELECT
  debut,type,
  count(distinct author) as new_developers,
  sum(new_developers) over (partition by type order by debut) as cum_new_developers
from news
  group by 1,2
order by 1 asc 

"""
    
 
st.experimental_memo(ttl=21600)
@st.cache
def compute(a):
    results=sdk.query(a)
    return results

results0 = compute(sql0)
df0 = pd.DataFrame(results0.records)
df0.info()

results00 = compute(sql00)
df00 = pd.DataFrame(results00.records)
df00.info()

results000 = compute(sql000)
df000 = pd.DataFrame(results000.records)
df000.info()

results = compute(sql)
df = pd.DataFrame(results.records)
df.info()

results2 = compute(sql2)
df2 = pd.DataFrame(results2.records)
df2.info()

results3 = compute(sql3)
df3 = pd.DataFrame(results3.records)
df3.info()

results4 = compute(sql4)
df4 = pd.DataFrame(results4.records)
df4.info()

results5 = compute(sql5)
df5 = pd.DataFrame(results5.records)
df5.info()

results6 = compute(sql6)
df6 = pd.DataFrame(results6.records)
df6.info()

# In[22]:

st.subheader('Type of Near developers by relationship')
st.write('The second batch metrics to be analyzed are the type of developers that are entering the Near protocol in the recent days,weeks and months based on the relationship with the protocol.')
st.write('Depending on the association with the project, each developer has a destined role which can be: **COLLABORATOR, FIRST_TIME_CONTRIBUTOR, MEMBER, OWNER or CONTRIBUTOR**.')
st.write('In concrete, the following charts shows:')
st.write('- Last month active and new developers by type (daily and cumulative)')
st.write('- Last 3 months active and new developers by type (weekly and cumulative)')
st.write('- Active and new developers over time by type (monthly and cumulative)')
st.write('')


import plotly.graph_objects as go
fig1 = go.Figure([go.Bar(x=df0['type'], y=df0['total_developers'],marker_color=px.colors.qualitative.Plotly)])
fig1.update_layout(
    title='Distribution of Near developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

fig2 = go.Figure([go.Bar(x=df00['type'], y=df00['total_developers'],marker_color=px.colors.qualitative.Vivid)])
fig2.update_layout(
    title='Distribution of Near developers by relationship in 2022',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)


# In[38]:


fig3 = go.Figure([go.Scatter(x=df000['type'], y=df000['total_developers'],marker_color=px.colors.qualitative.Plotly)])
fig3.update_layout(
    title='Distribution of Near developers by relationship in 2023',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.plotly_chart(fig3, theme="streamlit", use_container_width=True)

tab1, tab2, tab3 = st.tabs(["Developers by relationship so far", "Developers by relationship in 2022", "Developers by relationship in 2023"])

with tab1:
    st.plotly_chart(fig4, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig5, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig6, theme="streamlit", use_container_width=True)    
    

import plotly.express as px

fig1 = px.line(df, x="date", y="developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Daily active developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


fig2 = px.line(df2, x="date", y="developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Weekly active developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

fig3 = px.line(df3, x="date", y="developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig3.update_layout(
    title='Monthly active developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

tab1, tab2, tab3 = st.tabs(["Daily developers by relation", "Weekly developers by relation", "Monthly developers by relation"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)
    
    
    
fig1 = px.line(df, x="date", y="cum_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Total daily active developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


fig2 = px.line(df2, x="date", y="cum_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Total weekly active developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

fig3 = px.line(df3, x="date", y="cum_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig3.update_layout(
    title='Total monthly active developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

tab1, tab2, tab3 = st.tabs(["Total daily developers by relation", "Total weekly developers by relation", "Total monthly developers by relation"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)
    
    
    
    
    
    
fig1 = px.line(df4, x="date", y="new_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Daily new developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


fig2 = px.line(df5, x="date", y="new_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Weekly new developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

fig3 = px.line(df6, x="date", y="new_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig3.update_layout(
    title='Monthly new developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

tab1, tab2, tab3 = st.tabs(["Daily new developers by relation", "Weekly new developers by relation", "Monthly new developers by relation"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)
    
    
    
fig1 = px.line(df4, x="date", y="cum_new_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Total daily new developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


fig2 = px.line(df5, x="date", y="cum_new_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Total weekly new developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

fig3 = px.line(df6, x="date", y="cum_new_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig3.update_layout(
    title='Total monthly new developers by relationship',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

tab1, tab2, tab3 = st.tabs(["Total daily new developers by relation", "Total weekly new developers by relation", "Total monthly new developers by relation"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)

    
    

sql="""
with
activity as (
SELECT
  distinct author,
  trunc(updatedat,'month') as month,
  count(distinct updatedat) as counts,
  count(distinct id) as n_pulls,
  count(distinct repo) as n_repositories
  from near.beta.github_activity
  group by 1,2
  )
  select
  month as date,
  case when counts>10 then 'Full time'
  when counts between 2 and 10 then 'Part time'
  else 'One time' end as type,
  count(distinct author) as developers,
  sum(developers) over (partition by type order by month) as cum_developers,
  sum(n_pulls) as pulls,
  sum(pulls) over (partition by type order by month) as cum_pulls,
  sum(n_repositories) as repositories,
  sum(repositories) over (partition by type order by month) as cum_repositories
from activity
group by 1,2
order by 1 asc 
"""

sql2="""
with
activity as (
SELECT
  distinct author,
  trunc(updatedat,'month') as month,
  count(distinct updatedat) as counts,
  count(distinct id) as n_pulls,
  count(distinct repo) as n_repositories
  from near.beta.github_activity where month between '2022-01-01' and '2023-01-01'
  group by 1,2
  )
  select
  month as date,
  case when counts>10 then 'Full time'
  when counts between 2 and 10 then 'Part time'
  else 'One time' end as type,
  count(distinct author) as developers,
  sum(developers) over (partition by type order by month) as cum_developers,
  sum(n_pulls) as pulls,
  sum(pulls) over (partition by type order by month) as cum_pulls,
  sum(n_repositories) as repositories,
  sum(repositories) over (partition by type order by month) as cum_repositories
from activity
group by 1,2
order by 1 asc 
"""
    
@st.cache
def compute(a):
    results=sdk.query(a)
    return results

results = compute(sql)
df = pd.DataFrame(results.records)
df.info()

results2 = compute(sql2)
df2 = pd.DataFrame(results2.records)
df2.info()


# In[22]:

st.subheader('Type of Near developers by frequency of contribution')
st.write('The third batch metrics to be analyzed are the type of developers that are entering the Near protocol in the recent days,weeks and months based on the amount of activity are developing on the ecosystem.')
st.write('Depending on their frequency of contribution, each developer has a destined name:')
st.write('- Full time developer: active for 10 or more days per month')
st.write('- Part time developer: active for fewer than 10 days per month')
st.write('- One time developer: active just once')
st.write('')
st.write('In concrete, the following charts shows:')
st.write('- Active developers over time by type (monthly and cumulative)')
st.write('- Active repositories over time by type of developer (monthly and cumulative)')
st.write('- Active pulls over time by type of developer (monthly and cumulative)')
st.write('- Active developers over 2022')
st.write('- Active repositories over 2022')
st.write('- Active pulls over 2022')
st.write('')


fig1 = px.line(df, x="date", y="developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Monthly active developers by contribution',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


fig2 = px.line(df2, x="date", y="developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Active developers by contribution in 2022',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


tab1, tab2 = st.tabs(["Monthly developers by contribution", "Developers by contribution in 2022"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
    
    
fig1 = px.line(df, x="date", y="cum_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Total monthly developers by contribution',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


fig2 = px.line(df2, x="date", y="cum_developers", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Total developers in 2022 by contribution',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

tab1, tab2 = st.tabs(["Total monthly developers by contribution", "Total developers in 2022 by contribution"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
    
    
    
    
    
    
fig1 = px.line(df, x="date", y="repositories", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Monthly repositories by contributors',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


fig2 = px.line(df2, x="date", y="repositories", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Repositories by contributors in 2022',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


tab1, tab2 = st.tabs(["Monthly repositories by contributors", "Repositories by contributors in 2022"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
    
    
fig1 = px.line(df, x="date", y="cum_repositories", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Total monthly repositories by contributors',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


fig2 = px.line(df2, x="date", y="cum_repositories", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Total repositories in 2022 by contributors',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

tab1, tab2 = st.tabs(["Total monthly repositories by contributors", "Total repositories in 2022 by contributors"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
    
    
    

    
    
fig1 = px.line(df, x="date", y="pulls", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Monthly pull requests by contributors',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


fig2 = px.line(df2, x="date", y="pulls", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Pull requests by contributors in 2022',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


tab1, tab2 = st.tabs(["Monthly pulls by contributors", "Pulls by contributors in 2022"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
    
    
fig1 = px.line(df, x="date", y="cum_pulls", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Total monthly pull requests by contributors',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


fig2 = px.line(df2, x="date", y="cum_pulls", color="type", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Total pull requests in 2022 by contributors',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

tab1, tab2 = st.tabs(["Total monthly pulls by contributors", "Total pulls in 2022 by contributors"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
    
    
    


# In[16]:


sql = f"""
WITH
  price as (
  SELECT
  trunc(timestamp,'day') as date,
  avg(price_usd) as price_usd
  from near.core.fact_prices where symbol='wNEAR'
  group by 1
  ),
stats as (
SELECT
  trunc(updatedat,'day') as date,
  count(distinct author) as developers,
  sum(developers) over (order by date) as cum_developers,
count(distinct id) as pulls,
  sum(pulls) over (order by date) as cum_pulls,
  count(distinct repo) as repositories,
  sum(repositories) over (order by date) as cum_repositories
from near.beta.github_activity where date>=CURRENT_DATE-INTERVAL '1 MONTH'
  group by 1
order by 1 asc
  )
  SELECT
  p.date,
  developers,cum_developers,pulls,cum_pulls,repositories,cum_repositories,price_usd
  from stats s join price p on s.date=p.date
  order by 1 asc 
 
"""

sql2 = f"""
WITH
  price as (
  SELECT
  trunc(timestamp,'week') as date,
  avg(price_usd) as price_usd
  from near.core.fact_prices where symbol='wNEAR'
  group by 1
  ),
stats as (
SELECT
  trunc(updatedat,'week') as date,
  count(distinct author) as developers,
  sum(developers) over (order by date) as cum_developers,
count(distinct id) as pulls,
  sum(pulls) over (order by date) as cum_pulls,
  count(distinct repo) as repositories,
  sum(repositories) over (order by date) as cum_repositories
from near.beta.github_activity where date>=CURRENT_DATE-INTERVAL '3 MONTHS'
  group by 1
order by 1 asc
  )
  SELECT
  p.date,
  developers,cum_developers,pulls,cum_pulls,repositories,cum_repositories,price_usd
  from stats s join price p on s.date=p.date
  order by 1 asc


"""

sql3 = f"""
WITH
  price as (
  SELECT
  trunc(timestamp,'month') as date,
  avg(price_usd) as price_usd
  from near.core.fact_prices where symbol='wNEAR'
  group by 1
  ),
stats as (
SELECT
  trunc(updatedat,'month') as date,
  count(distinct author) as developers,
  sum(developers) over (order by date) as cum_developers,
count(distinct id) as pulls,
  sum(pulls) over (order by date) as cum_pulls,
  count(distinct repo) as repositories,
  sum(repositories) over (order by date) as cum_repositories
from near.beta.github_activity
  group by 1
order by 1 asc
  )
  SELECT
  p.date,
  developers,cum_developers,pulls,cum_pulls,repositories,cum_repositories,price_usd
  from stats s join price p on s.date=p.date
  order by 1 asc 

"""

sql4="""
WITH
  price as (
  SELECT
  trunc(timestamp,'day') as date,
  avg(price_usd) as price_usd
  from near.core.fact_prices where symbol='wNEAR'
  group by 1
  ),
news as (
  SELECT
  distinct author,
  min(trunc(createdat,'day')) as debut
  from near.beta.github_activity
  group by 1
  ),
  stats as (
  SELECT
  debut,
  count(distinct author) as new_developers,
  sum(new_developers) over (order by debut) as cum_new_developers
from news where debut>=CURRENT_DATE-INTERVAL '1 MONTH'
  group by 1
order by 1 asc 
  )
  SELECT
  p.date,
  new_developers,cum_new_developers,price_usd
  from stats s join price p on s.debut=p.date
  order by 1 asc  

"""

sql5="""
WITH
  price as (
  SELECT
  trunc(timestamp,'week') as date,
  avg(price_usd) as price_usd
  from near.core.fact_prices where symbol='wNEAR'
  group by 1
  ),
news as (
  SELECT
  distinct author,
  min(trunc(createdat,'week')) as debut
  from near.beta.github_activity
  group by 1
  ),
  stats as (
  SELECT
  debut,
  count(distinct author) as new_developers,
  sum(new_developers) over (order by debut) as cum_new_developers
from news where debut>=CURRENT_DATE-INTERVAL '3 MONTHS'
  group by 1
order by 1 asc 
  )
  SELECT
  p.date,
  new_developers,cum_new_developers,price_usd
  from stats s join price p on s.debut=p.date
  order by 1 asc 
"""

sql6="""
WITH
  price as (
  SELECT
  trunc(timestamp,'month') as date,
  avg(price_usd) as price_usd
  from near.core.fact_prices where symbol='wNEAR'
  group by 1
  ),
news as (
  SELECT
  distinct author,
  min(trunc(createdat,'month')) as debut
  from near.beta.github_activity
  group by 1
  ),
  stats as (
  SELECT
  debut,
  count(distinct author) as new_developers,
  sum(new_developers) over (order by debut) as cum_new_developers
from news
  group by 1
order by 1 asc 
  )
  SELECT
  p.date,
  new_developers,cum_new_developers,price_usd
  from stats s join price p on s.debut=p.date
  order by 1 asc 

"""


@st.cache
def compute(a):
    results=sdk.query(a)
    return results

results = compute(sql)
df = pd.DataFrame(results.records)
df.info()

results2 = compute(sql2)
df2 = pd.DataFrame(results2.records)
df2.info()

results3 = compute(sql3)
df3 = pd.DataFrame(results3.records)
df3.info()

results4 = compute(sql4)
df4 = pd.DataFrame(results4.records)
df4.info()

results5 = compute(sql5)
df5 = pd.DataFrame(results5.records)
df5.info()

results6 = compute(sql6)
df6 = pd.DataFrame(results6.records)
df6.info()

# In[22]:

st.subheader('Relationship between developers activity and NEAR price')
st.write('The fourth batch of metrics to be analyzed is the correlation between the developer activity against the NEAR price trend.')
st.write('In concrete, the following charts shows:')
st.write('- Active developers vs NEAR price')
st.write('- New developers vs NEAR price')
st.write('- Active repositories vs NEAR price')
st.write('- Active pulls vs NEAR price')
st.write('')



# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['date'],
                y=df['developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig1.add_trace(go.Line(x=df['date'],
                y=df['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig1.update_layout(
    title='Daily active developers vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig1.update_yaxes(title_text="Daily active developers", secondary_y=False)
fig1.update_yaxes(title_text="NEAR price evolution", secondary_y=True)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df2['date'],
                y=df2['developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df2['date'],
                y=df2['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Weekly developers vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig2.update_yaxes(title_text="Weekly active developers", secondary_y=False)
fig2.update_yaxes(title_text="NEAR price evolution", secondary_y=True)


# Create figure with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Bar(x=df3['date'],
                y=df3['developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig3.add_trace(go.Line(x=df3['date'],
                y=df3['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig3.update_layout(
    title='Monthly developers vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig3.update_yaxes(title_text="Monthly active developers", secondary_y=False)
fig3.update_yaxes(title_text="NEAR price evolution", secondary_y=True)

tab1, tab2, tab3 = st.tabs(["Daily developers vs NEAR", "Weekly developers vs NEAR", "Monthly developers vs NEAR"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)



# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df4['date'],
                y=df4['new_developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig1.add_trace(go.Line(x=df4['date'],
                y=df4['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig1.update_layout(
    title='Daily new developers vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig1.update_yaxes(title_text="Daily new developers", secondary_y=False)
fig1.update_yaxes(title_text="NEAR price evolution", secondary_y=True)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df5['date'],
                y=df5['new_developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df5['date'],
                y=df5['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Weekly new developers vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig2.update_yaxes(title_text="Weekly new developers", secondary_y=False)
fig2.update_yaxes(title_text="NEAR price evolution", secondary_y=True)


# Create figure with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Bar(x=df6['date'],
                y=df6['new_developers'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig3.add_trace(go.Line(x=df6['date'],
                y=df6['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig3.update_layout(
    title='Monthly new developers vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig3.update_yaxes(title_text="Monthly new developers", secondary_y=False)
fig3.update_yaxes(title_text="NEAR price evolution", secondary_y=True)

tab1, tab2, tab3 = st.tabs(["Daily new developers vs NEAR", "Weekly new developers vs NEAR", "Monthly new developers vs NEAR"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)




# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['date'],
                y=df['repositories'],
                name='# of repos',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig1.add_trace(go.Line(x=df['date'],
                y=df['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig1.update_layout(
    title='Daily active repos vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig1.update_yaxes(title_text="Daily active repos", secondary_y=False)
fig1.update_yaxes(title_text="NEAR price evolution", secondary_y=True)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df2['date'],
                y=df2['repositories'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df2['date'],
                y=df2['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Weekly repos vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig2.update_yaxes(title_text="Weekly active repos", secondary_y=False)
fig2.update_yaxes(title_text="NEAR price evolution", secondary_y=True)


# Create figure with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Bar(x=df3['date'],
                y=df3['repositories'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig3.add_trace(go.Line(x=df3['date'],
                y=df3['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig3.update_layout(
    title='Monthly repos vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig3.update_yaxes(title_text="Monthly active repos", secondary_y=False)
fig3.update_yaxes(title_text="NEAR price evolution", secondary_y=True)

tab1, tab2, tab3 = st.tabs(["Daily repos vs NEAR price", "Weekly repos vs NEAR price", "Monthly repos vs NEAR price"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)




    
# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['date'],
                y=df['pulls'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig1.add_trace(go.Line(x=df['date'],
                y=df['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig1.update_layout(
    title='Daily active pulls vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig1.update_yaxes(title_text="Daily active pulls", secondary_y=False)
fig1.update_yaxes(title_text="NEAR price evolution", secondary_y=True)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df2['date'],
                y=df2['pulls'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df2['date'],
                y=df2['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Weekly pulls vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig2.update_yaxes(title_text="Weekly active pulls", secondary_y=False)
fig2.update_yaxes(title_text="NEAR price evolution", secondary_y=True)


# Create figure with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Bar(x=df3['date'],
                y=df3['pulls'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig3.add_trace(go.Line(x=df3['date'],
                y=df3['price_usd'],
                name='USD price',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig3.update_layout(
    title='Monthly pulls vs NEAR price',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig3.update_yaxes(title_text="Monthly active pulls", secondary_y=False)
fig3.update_yaxes(title_text="NEAR price evolution", secondary_y=True)

tab1, tab2, tab3 = st.tabs(["Daily pull requests vs NEAR", "Weekly pull requests vs NEAR", "Monthly pull requests vs NEAR"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)





# In[17]:


## new users retained ultim mes
sql = f"""
WITH
  new_users as (
  SELECT
  distinct author as users,
  min(createdat::date) as debut
  from near.beta.github_activity
    where updatedat between CURRENT_DATE-INTERVAL '3 MONTH' and CURRENT_DATE-INTERVAL '2 MONTH'
  group by 1
  ),
  users_retention as (
SELECT
distinct author as users,
  updatedat::date as date
  from near.beta.github_activity
  where author in (select users from new_users)
  and updatedat >=CURRENT_DATE-INTERVAL '1 MONTH'
  )
select 
count(distinct x.users) as total_users,
count(distinct y.users) as retained_users,
(retained_users/total_users)*100 as pcg_retention
from new_users x, users_retention y
"""

## retention by days to rejoin
sql2 = f"""
--credits to hess
with final as 
  (select (updatedat) as date, author as user
from near.beta.github_activity
),
final_2 as 
  ( select lag(date, 1) ignore nulls over (partition by user order by date asc) as tx_date,
datediff('day',tx_date, date) as n_days, user
from final
qualify tx_date is not null
)
select count(DISTINCT(user)) as total_user,
case when n_days = 0 then 'Same Day'
when n_days = 1 then '1 Day'
when n_days between 1 and 7 then 'Less than a week'
when n_days between 8 and 30 then 'Less than a month'
when n_days between 31 and 60 then 'After a month'
when n_days between 61 and 90 then 'After Two months'
when n_days between 91 and 120 then 'After Three months'
when n_days between 121 and 150 then 'After Four months'
when n_days between 151 and 180 then 'After Five months'
when n_days between 181 and 210 then 'After Six months'
when n_days > 210 then 'More than six months' end as duration 
from final_2
group by 2

"""

## daily user retention over time
sql3="""
with retention as (
  SELECT
  author,
  updatedat,
  trunc(updatedat,'day') as date,
  rank() over (partition by author order by date asc) as rank
  from near.beta.github_activity
)
SELECT
date, count(distinct author) as retained_users from retention where rank>1 and date>=current_date- INTERVAL '1 MONTH'
group by 1 order by 1

"""

## weekly user retention over time
sql4="""
with retention as (
  SELECT
  author,
  updatedat,
  trunc(updatedat,'week') as date,
  rank() over (partition by author order by date asc) as rank
  from near.beta.github_activity
)
SELECT
date, count(distinct author) as retained_users from retention where rank>1 and date>=current_date- INTERVAL '3 MONTHS'
group by 1 order by 1

"""

## monthly user retention over time
sql5="""
with retention as (
  SELECT
  author,
  updatedat,
  trunc(updatedat,'month') as date,
  rank() over (partition by author order by date asc) as rank
  from near.beta.github_activity
)
SELECT
date, count(distinct author) as retained_users from retention where rank>1
group by 1 order by 1

"""



@st.cache
def compute(a):
    results=sdk.query(a)
    return results

results = compute(sql)
df = pd.DataFrame(results.records)
df.info()

results2 = compute(sql2)
df2 = pd.DataFrame(results2.records)
df2.info()

results3 = compute(sql3)
df3 = pd.DataFrame(results3.records)
df3.info()

results4 = compute(sql4)
df4 = pd.DataFrame(results4.records)
df4.info()

results5 = compute(sql5)
df5 = pd.DataFrame(results5.records)
df5.info()

# In[22]:

st.subheader('Near developer retention')
st.write('The final batch of metrics to be analyzed are those related to the Near developer retention.')
st.write('In concrete, the following charts shows:')
st.write('- User retention over the past month')
st.write('- Daily developer retention over the past month')
st.write('- Weekly developer retention over the past 3 months')
st.write('- Monthly developer retention over time')
st.write('- Distribution of developers by time retained')
st.write('')

col1,col2,col3 =st.columns(3)
with col1:
    st.metric('Total Near developers', millify(df['total_users'][0]))
col2.metric('Retained developers over the past month', millify(df['retained_users'][0]))
col3.metric('% developers retained over the past month', millify(df['pcg_retention'][0]))


# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Line(x=df3['date'],
                y=df3['retained_users'],
                name='# of devs',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))

fig1.update_layout(
    title='Daily developer retention over the past month',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig1.update_yaxes(title_text="Daily developer retention", secondary_y=False)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df4['date'],
                y=df4['retained_users'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))

fig2.update_layout(
    title='Weekly developer retention over the past 3 months',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig2.update_yaxes(title_text="Weekly developer retention", secondary_y=False)


# Create figure with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Bar(x=df5['date'],
                y=df5['retained_users'],
                name='# of users',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))

fig3.update_layout(
    title='Monthly developer retention over time',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

# Set y-axes titles
fig3.update_yaxes(title_text="Monthly developer retention", secondary_y=False)

tab1, tab2, tab3 = st.tabs(["Daily developer retention", "Weekly developer retention", "Monthly developer retention"])

with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    
with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)


fig1 = px.line(df2, x="duration", y="total_user", color="duration", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Distribution of developers by retention time',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.plotly_chart(fig1, theme="streamlit", use_container_width=True)





st.subheader('Conclusions')
st.markdown('Following the Near Foundation Weekly Transparency Report and using Flipside Crypto and MetricsDAO data, I have been able to develop a tool that tracks Near activity in a more user-friendly and clean way.')
st.markdown('The most interesting thing I have found is the way in which the activity takes place in NEAR. It seems that users tend to use the ecosystem more during specific hours. The peaks seems to be registered from 5:00PM to 8:00PM. The same pattern holds true for active users, transactions and gas used!')
st.markdown('Furhtermore, the activity since to be increased during the last week in which users, transactions and gas used have been doubled!')
st.write('')
st.markdown('This app has been done by **_Adrià Parcerisas_**, a PhD Biomedical Engineer related to Machine Learning and Artificial intelligence technical projects for data analysis and research, as well as dive deep on-chain data analysis about cryptocurrency projects. You can find me on [Twitter](https://twitter.com/adriaparcerisas)')
st.write('')
st.markdown('The full sources used to develop this app can be found to the following link: [Github link](https://github.com/adriaparcerisas/Near-developer-activity)')
st.markdown('_Powered by [Flipside Crypto](https://flipsidecrypto.xyz) and [MetricsDAO](https://metricsdao.notion.site)_')


# In[ ]:






# In[ ]:




