"""Fotografa le demo vere con Chromium: telefono (390x844) o computer (1280x800), scala 2."""
import sys, os, json, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
VIEW = {'w10': (1000, 700), 'vid': (1280, 720), 'tel': (390, 844), 'web': (1280, 800), 'tab': (900, 1100), 'a4': (794, 1123)}

async def main(jobs):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, page_file, hash_, kind, actions in jobs:
            w, h = VIEW[kind]
            ctx = await b.new_context(viewport={'width': w, 'height': h}, device_scale_factor=2)
            pg = await ctx.new_page()
            await pg.goto('file://' + os.path.join(HERE, 'demo', page_file) + (('#' + hash_) if hash_ else ''))
            await pg.wait_for_timeout(300)
            for a in actions or []:
                if a[0] == 'click':
                    await pg.click(a[1])
                elif a[0] == 'fill':
                    await pg.fill(a[1], a[2])
                elif a[0] == 'js':
                    await pg.evaluate(a[1])
                elif a[0] == 'wait':
                    await pg.wait_for_timeout(a[1])
                await pg.wait_for_timeout(120)
            await pg.screenshot(path=os.path.join(HERE, 'shots', name + '.png'))
            await ctx.close()
        await b.close()

if __name__ == '__main__':
    jobs = json.load(open(sys.argv[1]))
    asyncio.run(main(jobs))
