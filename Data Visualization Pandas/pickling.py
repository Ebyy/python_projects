import quandl
import pandas as pd
import pickle

api_key = "yhJYCBmdSnc4psSPtuYt"

def state_list():
    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fifty_states[0][0][1:]

def grab_initial_state_data():
    main_df = pd.DataFrame()

    for abbv in fifty_states[0][0][1:]:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        # df.columns = [str(abbv)] -->instead of equating rsuffix

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, rsuffix=abbv)

    print(main_df.head())

    pickle_out = open('fifty_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

pickle_in = open('fifty_states.pickle', 'rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)

#OR to use the panda pickle
HPI_data.to_pickle('HPI.pickle')
HPI_data2 = pd.read_pickle('HPI.pickle')

