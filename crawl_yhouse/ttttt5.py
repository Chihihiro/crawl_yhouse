import asyncio
import time,random
from pyppeteer.launcher import launch # 控制模拟浏览器用
# from retrying import retry #设置重试次数用的

def main(url):# 定义main协程函数，
    #以下使用await 可以针对耗时的操作进行挂起

    browser = launch({'headless': False, 'args': ['--no-sandbox'], }) # 启动pyppeteer 属于内存中实现交互的模拟器
    page = browser.newPage()  # 启动个新的浏览器页面
    page.setUserAgent('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')

    page.goto(url) # 访问登录页面
    # 替换淘宝在检测浏览时采集的一些参数。
    # 就是在浏览器运行的时候，始终让window.navigator.webdriver=false
    # navigator是windiw对象的一个属性，同时修改plugins，languages，navigator 且让
    page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''') #以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
    page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')

    # 使用type选定页面元素，并修改其数值，用于输入账号密码，修改的速度仿人类操作，因为有个输入速度的检测机制
    # 因为 pyppeteer 框架需要转换为js操作，而js和python的类型定义不同，所以写法与参数要用字典，类型导入
    # await page.type('.J_UserName', username, {'delay': input_time_random() - 50})
    # await page.type('#J_StandardPwd input', pwd, {'delay': input_time_random()})

    #await page.screenshot({'path': './headless-pytt-result.png'})    # 截图测试
    time.sleep(2)

    # 检测页面是否有滑块。原理是检测页面元素。
    # slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块

    # if slider:
    #     print('当前页面出现滑块')
        #await page.screenshot({'path': './headless-login-slide.png'}) # 截图测试
        # flag,page = await mouse_slide(page=page) #js拉动滑块过去。
        # if flag:
        #     await page.keyboard.press('Enter') # 确保内容输入完毕，少数页面会自动完成按钮点击
        #     print("print enter",flag)
    data = page.evaluate('window.localStorage.roomparams;') # 如果无法通过回车键完成点击，就调用js模拟点击登录按钮。
    print(data)
    # time.sleep(2)
    # cookies_list = await page.cookies()
    # print(cookies_list)
    # await get_cookie(page) # 导出cookie 完成登陆后就可以拿着cookie玩各种各样的事情了。
    #
    # await page.evaluate('''document.getElementById("J_SubmitStatic").click()''')
    # await page.waitFor(20)
    # await page.waitForNavigation()





#
# if __name__ == '__main__':
#     url = 'http://hotel.elong.com/52001128/'
#     main(url)



# import asyncio
# import pyppeteer
# import os
#
# os.environ['PYPPETEER_CHROMIUM_REVISION'] = '588429'
# pyppeteer.DEBUG = True
#
#
# async def main():
#     print("in main ")
#     print(os.environ.get('PYPPETEER_CHROMIUM_REVISION'))
#     browser = await pyppeteer.launch()
#     page = await browser.newPage()
#     await page.goto('http://www.baidu.com')
#
#     content = await page.content()
#     cookies = await page.cookies()
#     # await page.screenshot({'path': 'example.png'})
#     await browser.close()
#     return {'content': content, 'cookies': cookies}
#
#
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(main())
# loop.run_until_complete(task)
#
# print(task.result())