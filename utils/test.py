# import js2py

# js = """../static/js/test.js""" 

# context = js2py.EvalJs()
# context.execute(js)
# print(context.output)
import execjs


print(execjs.eval("'red yellow blue'.split(' ')"))

ctx = execjs.compile("""
     function add(x, y) {
           return x + y;
        }

""")

print(ctx.call("add", 1, 2))