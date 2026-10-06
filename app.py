from flask import Flask, render_template, request, redirect, url_for
from db import get_connection

app = Flask(__name__)


def consultar(sql, params=()):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(sql, params)
    datos = cur.fetchall()
    cur.close()
    conn.close()
    return datos


def ejecutar(sql, params):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def inicio():
    return redirect(url_for("read"))


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        ejecutar(
            "INSERT INTO productos (nombre, precio, stock, id_categoria) VALUES (%s, %s, %s, %s)",
            (request.form["nombre"], request.form["precio"],
             request.form["stock"], request.form["id_categoria"])
        )
        return redirect(url_for("read"))
    categorias = consultar("SELECT * FROM categorias")
    return render_template("create.html", categorias=categorias)


@app.route("/read")
def read():
    productos = consultar(
        "SELECT p.id_producto, p.nombre, p.precio, p.stock, c.nombre AS categoria "
        "FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria"
    )
    return render_template("read.html", productos=productos)


@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        ejecutar(
            "UPDATE productos SET nombre=%s, precio=%s, stock=%s, id_categoria=%s WHERE id_producto=%s",
            (request.form["nombre"], request.form["precio"], request.form["stock"],
             request.form["id_categoria"], request.form["id_producto"])
        )
        return redirect(url_for("read"))
    categorias = consultar("SELECT * FROM categorias")
    producto = None
    id_producto = request.args.get("id")
    if id_producto:
        datos = consultar("SELECT * FROM productos WHERE id_producto = %s", (id_producto,))
        producto = datos[0] if datos else None
    return render_template("update.html", producto=producto, categorias=categorias)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        ejecutar("DELETE FROM productos WHERE id_producto = %s", (request.form["id_producto"],))
        return redirect(url_for("read"))
    producto = None
    id_producto = request.args.get("id")
    if id_producto:
        datos = consultar(
            "SELECT p.id_producto, p.nombre, p.precio, p.stock, c.nombre AS categoria "
            "FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria "
            "WHERE p.id_producto = %s", (id_producto,)
        )
        producto = datos[0] if datos else None
    return render_template("delete.html", producto=producto)


if __name__ == "__main__":
    app.run(debug=True)