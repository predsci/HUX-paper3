import datetime as dt


def get_time_interval(case_study):
    starttime, endtime, cr = None, None, None
    # set up - latitude minimum difference.
    if case_study == "cr2209":
        # Carrington Rotation 2209
        # Min lat 01 (2018-10-16)
        # 2018 Sep 29	2018 Oct 26
        starttime = dt.datetime(year=2018, month=9, day=29)
        endtime = dt.datetime(year=2018, month=10, day=26)
        cr = "2209"

    elif case_study == "cr2210":
        # Carrington Rotation 2210
        # 2018 Oct 26	2018 Nov 23
        # Min lat 02 (2018-11-22)
        # Encounter 1 date: 2018-11-06. Distance from the center of the sun: 0.17 au (35.6 RS)
        starttime = dt.datetime(year=2018, month=10, day=26)
        endtime = dt.datetime(year=2018, month=11, day=23)
        cr = "2210"

    elif case_study == "cr2211":
        # Carrington Rotation 2211
        # 2018 Nov 23	2018 Dec 20
        starttime = dt.datetime(year=2018, month=11, day=23)
        endtime = dt.datetime(year=2018, month=12, day=20)
        cr = "2211"

    elif case_study == "cr2215":
        # Carrington Rotation 2215
        # Min lat 03 (2019-04-05)
        # 2019 Mar 12	2019 Apr 08
        # Encounter 2 date: 2019-04-04. Distance from the center of the sun: 0.17 au (35.6 RS)
        starttime = dt.datetime(year=2019, month=3, day=12)
        endtime = dt.datetime(year=2019, month=4, day=8)
        cr = "2215"

    elif case_study == "cr2219":
        # Carrington Rotation 2219
        # Min lat 04 (2019-07-12)
        # 2019 Jun 29	2019 Jul 26
        starttime = dt.datetime(year=2019, month=6, day=29)
        endtime = dt.datetime(year=2019, month=7, day=26)
        cr = "2219"

    elif case_study == "cr2221":
        # Carrington Rotation 2221
        # 2019 Aug 22	2019 Sep 19
        # Encounter 3 date: 2019-09-01. Distance from the center of the sun: 0.17 au (35.6 RS)
        starttime = dt.datetime(year=2019, month=8, day=22)
        endtime = dt.datetime(year=2019, month=9, day=19)
        cr = "2221"

    elif case_study == "cr2223":
        # Carrington Rotation 2223
        # 2019 Oct 16	2019 Nov 12
        # Min 05 (2019-11-05)
        starttime = dt.datetime(year=2019, month=10, day=16)
        endtime = dt.datetime(year=2019, month=11, day=12)
        cr = "2223"

    elif case_study == "cr2226":
        # todo: PSP VR DATA IS NOT AVAILABLE.
        # Carrington Rotation 2226
        # 2020 Jan 06	2020 Feb 02
        # Encounter 4 date: 2020-01-29. Distance from the center of the sun: 0.13 au (27.8 RS)
        starttime = dt.datetime(year=2020, month=1, day=6)
        endtime = dt.datetime(year=2020, month=2, day=2)
        cr = "2226"

    elif case_study == "cr2231":
        # Carrington Rotation 2231
        # 2020 May 21	2020 Jun 18
        # Encounter 5 date: 2020-06-07. Distance from the center of the sun: 0.13 au (27.8 RS)
        starttime = dt.datetime(year=2020, month=5, day=21)
        endtime = dt.datetime(year=2020, month=6, day=18)
        cr = "2231"

    elif case_study == "cr2232":
        # Carrington Rotation 2232 (Solo aligned with Earth)
        # 2020 Jun 18 to 2020 Jul 15
        starttime = dt.datetime(year=2020, month=6, day=18)
        endtime = dt.datetime(year=2020, month=7, day=15)
        cr = "2232"

    elif case_study == "cr2233":
        # Carrington Rotation 2233 (Solo available data)
        # 2020 Jul 15 to 2020 Aug 11
        starttime = dt.datetime(year=2020, month=7, day=15)
        endtime = dt.datetime(year=2020, month=8, day=11)
        cr = "2233"

    elif case_study == "cr2234":
        # Carrington Rotation 2234 (Solo available data)
        # 2020 Aug 11 to 2020 Sep 07
        starttime = dt.datetime(year=2020, month=8, day=11)
        endtime = dt.datetime(year=2020, month=9, day=7)
        cr = "2234"

    elif case_study == "cr2235":
        # todo: PSP VR DATA IS NOT AVAILABLE.
        # Carrington Rotation 2235
        # 2020 Sep 07	2020 Oct 05
        # Encounter 6 date: 2020-09-27. Distance from the center of the sun: 0.09 au (20.3 RS)
        starttime = dt.datetime(year=2020, month=9, day=7)
        endtime = dt.datetime(year=2020, month=10, day=5)
        cr = "2235"

    elif case_study == "cr2238":
        # Carrington Rotation 2238
        # 2020 Nov 28 to 2020 Dec 25
        starttime = dt.datetime(year=2020, month=11, day=28)
        endtime = dt.datetime(year=2020, month=12, day=25)
        cr = "2238"

    elif case_study == "cr2239":
        # todo: PSP VR DATA IS NOT AVAILABLE.
        # Carrington Rotation 2239
        # 2020 Dec 25	2021 Jan 22
        # Encounter 7 date: 2021-01-17. Distance from the center of the sun: 0.09 au (20.3 RS)
        starttime = dt.datetime(year=2020, month=12, day=25)
        endtime = dt.datetime(year=2021, month=1, day=22)
        cr = "2239"

    return starttime, endtime, cr