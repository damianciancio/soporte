import pymysql


class AccesoDatos():

    conn = None
    cur = None

    def conectar(self):
        try:
            self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='soporte')
            self.cur = self.conn.cursor()
        except Exception as e:
            raise e
        return self.cur

    def desconectar(self):
        try:
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        except Exception:
            raise

