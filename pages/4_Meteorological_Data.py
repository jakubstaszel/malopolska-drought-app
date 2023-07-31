import streamlit as st
import pandas as pd

data_json = {"date":{"0":"2019-01-01","1":"2019-02-01","2":"2019-03-01","3":"2019-04-01","4":"2019-05-01","5":"2019-06-01","6":"2019-07-01","7":"2019-08-01","8":"2019-09-01","9":"2019-10-01","10":"2019-11-01","11":"2019-12-01","12":"2020-01-01","13":"2020-02-01","14":"2020-03-01","15":"2020-04-01","16":"2020-05-01","17":"2020-06-01","18":"2020-07-01","19":"2020-08-01","20":"2020-09-01","21":"2020-10-01","22":"2020-11-01","23":"2020-12-01","24":"2021-01-01","25":"2021-02-01","26":"2021-03-01","27":"2021-04-01","28":"2021-05-01","29":"2021-06-01","30":"2021-07-01","31":"2021-08-01","32":"2021-09-01","33":"2021-10-01","34":"2021-11-01","35":"2021-12-01","36":"2022-01-01","37":"2022-02-01","38":"2022-03-01","39":"2022-04-01","40":"2022-05-01","41":"2022-06-01","42":"2022-07-01","43":"2022-08-01","44":"2022-09-01","45":"2022-10-01","46":"2022-11-01","47":"2022-12-01"},"precip":{"0":52.6,"1":13.4,"2":23.9,"3":72.7,"4":124.9,"5":4.2,"6":74.7,"7":79.3,"8":78.3,"9":35.5,"10":43.3,"11":35.7,"12":20.5,"13":75.8,"14":15.2,"15":4.4,"16":88.3,"17":72.9,"18":65.5,"19":108.6,"20":79.2,"21":95.9,"22":23.3,"23":22.2,"24":40.1,"25":35.4,"26":18.2,"27":65.5,"28":76.4,"29":73.5,"30":142.7,"31":192.0,"32":39.9,"33":15.9,"34":44.0,"35":31.3,"36":36.8,"37":44.6,"38":17.0,"39":28.5,"40":16.4,"41":57.2,"42":87.1,"43":117.0,"44":64.9,"45":21.6,"46":38.5,"47":63.1}}

data_json = {"date":{"0":"01","1":"02","2":"03","3":"04","4":"05","5":"06","6":"07","7":"08","8":"09","9":"10","10":"11","11":"12"},"precip":{"0":37.5,"1":42.3,"2":18.575,"3":42.775,"4":76.5,"5":51.95,"6":92.5,"7":124.225,"8":65.575,"9":42.225,"10":37.275,"11":38.075}}
st.bar_chart(pd.DataFrame(data_json).set_index('date'))

data_json_2 = {"date":{"0":"01","1":"02","2":"03","3":"04","4":"05","5":"06","6":"07","7":"08","8":"09","9":"10","10":"11","11":"12"},"temp":{"0":-0.35,"1":2.275,"2":4.5,"3":8.2,"4":12.8,"5":19.875,"6":19.775,"7":19.65,"8":14.2,"9":10.1,"10":4.975,"11":0.95}}
st.bar_chart(pd.DataFrame(data_json_2).set_index('date'))

data_json_3 = {"date":{"0":"01","1":"02","2":"03","3":"04","4":"05","5":"06","6":"07","7":"08","8":"09","9":"10","10":"11","11":"12"},"precip":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0},"precip2":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0},"precip3":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0},"temp":{"0":-0.35,"1":2.275,"2":4.5,"3":8.2,"4":12.8,"5":19.875,"6":19.775,"7":19.65,"8":14.2,"9":10.1,"10":4.975,"11":0.95}}
st.bar_chart(pd.DataFrame(data_json_3).set_index('date'))