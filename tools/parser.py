import numpy as np

def convert_int(x,extract_pos=False): # splits a single string to int
#     print(x.split(" "))
    if extract_pos:
        print(x.split(" "))
        return [int(i) for i in list(filter(None,x.split(" ")))],
    else:
        return [int(i) for i in list(filter(None,x.split(" ")))]



#map to linearize ADC values
qiecodes=np.asarray([1.58,   4.73,   7.88,   11.0,   14.2,   17.3,   20.5,   23.6,
          26.8,   29.9,   33.1,   36.2,   39.4,   42.5,   45.7,   48.8,
          53.6,   60.1,   66.6,   73.0,   79.5,   86.0,   92.5,   98.9,
          105,    112,    118,    125,    131,    138,    144,    151,
          157,    164,    170,    177,    186,    199,    212,    225,
          238,    251,    264,    277,    289,    302,    315,    328,
          341,    354,    367,    380,    393,    406,    418,    431,
          444,    464,    490,    516,    542,    568,    594,    620,
          569,    594,    619,    645,    670,    695,    720,    745,
          771,    796,    821,    846,    871,    897,    922,    947,
          960,    1010,   1060,   1120,   1170,   1220,   1270,   1320,
          1370,   1430,   1480,   1530,   1580,   1630,   1690,   1740,
          1790,   1840,   1890,   1940,   2020,   2120,   2230,   2330,
          2430,   2540,   2640,   2740,   2850,   2950,   3050,   3150,
          3260,   3360,   3460,   3570,   3670,   3770,   3880,   3980,
          4080,   4240,   4450,   4650,   4860,   5070,   5280,   5490,
          5080,   5280,   5480,   5680,   5880,   6080,   6280,   6480,
          6680,   6890,   7090,   7290,   7490,   7690,   7890,   8090,
          8400,   8810,   9220,   9630,   10000,  10400,  10900,  11300,
          11700,  12100,  12500,  12900,  13300,  13700,  14100,  14500,
          15000,  15400,  15800,  16200,  16800,  17600,  18400,  19300,
          20100,  20900,  21700,  22500,  23400,  24200,  25000,  25800,
          26600,  27500,  28300,  29100,  29900,  30700,  31600,  32400,
          33200,  34400,  36100,  37700,  39400,  41000,  42700,  44300,
          41100,  42700,  44300,  45900,  47600,  49200,  50800,  52500,
          54100,  55700,  57400,  59000,  60600,  62200,  63900,  65500,
          68000,  71300,  74700,  78000,  81400,  84700,  88000,  91400,
          94700,  98100,  101000, 105000, 108000, 111000, 115000, 118000,
          121000, 125000, 128000, 131000, 137000, 145000, 152000, 160000,
          168000, 176000, 183000, 191000, 199000, 206000, 214000, 222000,
          230000, 237000, 245000, 253000, 261000, 268000, 276000, 284000,
          291000, 302000, 316000, 329000, 343000, 356000, 370000, 384000, 398000])

def parse_text_file(file_name, start_event=0, stop_event=-1): #expects a certain type of data, proceed with caution
    if (stop_event == -1): stop_flag = False #disable stop event
    else: stop_flag = True #enable stop event
    with open(file_name) as f: #loading file into memory
        lines = f.readlines()  
    evt_status = ""
    data = []
    l = lines # renaming so it is easier to type
    i=0
    TDC = []
    TDC2 = [] # if the threhold was crossed prior to recording
    BX = []
    AMPL = []
    CH = []
    while(i < len(l)):
        if ("---------------------------------------------------------------------------" in l[i]):
            i = i + 1 #skip one line
            continue
        if ("--- START" in l[i]): #parse the event information
            evt_stat = list(filter(None,l[i].split(" ")))
            #print(evt_stat) #debugging
            #collect evt information
            evt_no = int(evt_stat[3][:-1])
            bx_no = int(evt_stat[5][:-1])
            orbit_no = int(evt_stat[7][:-1])
            run_no = int(evt_stat[9][:-1])
            i = i+1 #skip one line
#             print(evt_no,bx_no,orbit_no,run_no) #debugging
        else:
            if (evt_no > start_event): # start from event number 
                if ((evt_no > stop_event)&(stop_flag)): break # break if the events exceed stop event
#                 data = convert_int(l[i]) #convert strings to integer list
                try:
                    if ( len(l[i+1].strip()) > 0): #if TDC triggered
                        data = convert_int(l[i][:-1])
                        AMPL.append(data[2:])
                        CH.append(data[:2])
                        tdc = convert_int(l[i+1][:-1])
                        BX.append(bx_no)
                        TDC.append(tdc[0])
                except:
                    print (l[i][:-1])
            i = i+2 #skip lines
    return np.asarray(CH),np.asarray(AMPL),np.asarray(TDC),np.asarray(BX)

