def main():
    import tercol as _tercol
    import colorsys as _colorsys
    for hue in range(360):
        try:
            hue = float(hue)
            rgb = _colorsys.hsv_to_rgb(hue/360.0, 100.0/100.0, 100.0/100.0)
            print(_tercol.rgb(int(rgb[0]*256), int(rgb[1]*256), int(rgb[2]*256), 'COLOR'), end='\r')
        except KeyboardInterrupt: break
  
if __name__ == '__main__':
    main()