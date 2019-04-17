from bottle import route, run
import sqlite3
import json

db_file = '/home/zhaoyongli/workspace/AuboApplicationBuildDir/OUR4.0-I5-Build/bin/Database/tool_coord_param.db'


@route('/api/gettool', method=['GET', 'POST'])
def gettool():

    db_conn = sqlite3.connect(db_file)
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT * FROM tool_param_view")
    records = db_cursor.fetchall()
    db_cursor.close()

    if not records:
        return {}
    else:
        data = []
        for record in records:
            tmp = []
            # tool name
            tmp.append({"tool_name": record[0]})
            # pos
            tmp.append({"x": record[2]})
            tmp.append({"y": record[3]})
            tmp.append({"z": record[3]})
            # ori
            tmp.append({"rx": record[4]})
            tmp.append({"ry": record[5]})
            tmp.append({"rz": record[6]})
            # add record
            data.append(tmp)

        # print(data)
        return json.dumps(data)
        # return json.dumps(data, default=lambda obj: obj.__dict__, sort_keys=True)


@route('/api/getcoord', method=['GET', 'POST'])
def getcoord():

    db_conn = sqlite3.connect(db_file)
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT * FROM coord_param_View")
    records = db_cursor.fetchall()
    db_cursor.close()

    if not records:
        return {}
    else:
        data = []
        for record in records:
            tmp = []
            # coord name
            tmp.append({"coord_name": record[0]})
            # method
            tmp.append({"method": record[1]})
            # 3 waypoints
            tmp.append({"point1": record[2]})
            tmp.append({"point2": record[3]})
            tmp.append({"point3": record[4]})
            # tool name
            tmp.append({"tool_name": record[5]})
            # pos
            tmp.append({"x": record[6]})
            tmp.append({"y": record[7]})
            tmp.append({"z": record[8]})
            # ori
            tmp.append({"rx": record[9]})
            tmp.append({"ry": record[10]})
            tmp.append({"rz": record[11]})
            # add record
            data.append(tmp)

        # print(data)
        return json.dumps(data)


if __name__ == "__main__":
    run(host='0.0.0.0', port=8080, reloader=True)
