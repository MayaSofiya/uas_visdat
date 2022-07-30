import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Maya Sofiya Intantri - 1900018298')
st.header('Data Penindakan Pelanggaran Lalu Lintas dan Angkutan Jalan tahun 2021')
#st.subheader('tahun 2021')

### --- LOAD DATAFRAME
excel_file = 'data_penindakan_pelanggaran.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:J',
                   header=0)

df_totalpelanggaran = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='L:M',
                                header=0)
df_totalpelanggaran.dropna(inplace=True)

###################
#-----STREAMLIT SELECTION menggunakan ocp_roda_dua min dan max
wilayah = df['wilayah'].unique().tolist()
pelanggaran = df['ocp_roda_dua'].unique().tolist()

ocp_roda_dua_selection = st.slider('Pilih Total Jumlah Pelanggaran: ',
                                min_value= min(pelanggaran),
                                max_value= max (pelanggaran),
                                value=(min(pelanggaran),max (pelanggaran)))

wilayah_selection = st.multiselect('Wilayah: ',
                                wilayah,
                                default=wilayah)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['ocp_roda_dua'].between(*ocp_roda_dua_selection)) & (df['wilayah'].isin(wilayah_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['wilayah']).sum()[['bap_tilang']]
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped, 
             x='wilayah', 
             y= 'bap_tilang',
             color_discrete_sequence =['#3399FF']*len(df_grouped),
             template= 'plotly_white')
st.plotly_chart(bar_chart)


###############
#-----STREAMLIT SELECTION stop_operasi
wilayah = df['wilayah'].unique().tolist()
pelanggaran2 = df['stop_operasi'].unique().tolist()

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['wilayah']).sum()[['stop_operasi']]
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped, 
             x='wilayah', 
             y= 'stop_operasi',
             color_discrete_sequence =['#3399FF']*len(df_grouped),
             template= 'plotly_white')
st.plotly_chart(bar_chart)

###############
#-----STREAMLIT SELECTION bap_polisi
wilayah = df['wilayah'].unique().tolist()
pelanggaran2 = df['bap_polisi'].unique().tolist()

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['wilayah']).sum()[['bap_polisi']]
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped, 
             x='wilayah', 
             y= 'bap_polisi',
             color_discrete_sequence =['#3399FF']*len(df_grouped),
             template= 'plotly_white')
st.plotly_chart(bar_chart)

###############
#-----STREAMLIT SELECTION stop_operasi_polisi
wilayah = df['wilayah'].unique().tolist()
pelanggaran2 = df['stop_operasi_polisi'].unique().tolist()

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['wilayah']).sum()[['stop_operasi_polisi']]
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped, 
             x='wilayah', 
             y= 'stop_operasi_polisi',
             color_discrete_sequence =['#3399FF']*len(df_grouped),
             template= 'plotly_white')
st.plotly_chart(bar_chart)

###############
#-----STREAMLIT SELECTION penderekan
wilayah = df['wilayah'].unique().tolist()
pelanggaran2 = df['penderekan'].unique().tolist()

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['wilayah']).sum()[['penderekan']]
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped, 
             x='wilayah', 
             y= 'penderekan',
             color_discrete_sequence =['#3399FF']*len(df_grouped),
             template= 'plotly_white')
st.plotly_chart(bar_chart)

###############
#-----STREAMLIT SELECTION ocp_roda_dua
wilayah = df['wilayah'].unique().tolist()
pelanggaran2 = df['ocp_roda_dua'].unique().tolist()

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['wilayah']).sum()[['ocp_roda_dua']]
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped, 
             x='wilayah', 
             y= 'ocp_roda_dua',
             color_discrete_sequence =['#3399FF']*len(df_grouped),
             template= 'plotly_white')
st.plotly_chart(bar_chart)

###############
#-----STREAMLIT SELECTION ocp_roda_empat
wilayah = df['wilayah'].unique().tolist()
pelanggaran2 = df['ocp_roda_empat'].unique().tolist()

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['wilayah']).sum()[['ocp_roda_empat']]
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped, 
             x='wilayah', 
             y= 'ocp_roda_empat',
             color_discrete_sequence =['#3399FF']*len(df_grouped),
             template= 'plotly_white')
st.plotly_chart(bar_chart)


###############
#-----STREAMLIT SELECTION angkut_motor
wilayah = df['wilayah'].unique().tolist()
pelanggaran2 = df['angkut_motor'].unique().tolist()

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['wilayah']).sum()[['angkut_motor']]
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped, 
             x='wilayah', 
             y= 'angkut_motor',
             color_discrete_sequence =['#3399FF']*len(df_grouped),
             template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- PLOT PIE CHART
pie_chart = px.pie(df_totalpelanggaran,
                title='Total jumlah pelanggaran per Bulan',
                values='totalpelanggaran',
                names='padabulan',)

st.plotly_chart(pie_chart)


image = Image.open('images/logo2.jpg')
st.image(image,
        caption='Designed by Maya / UAS Visualisasi Data',
        use_column_width=True)
