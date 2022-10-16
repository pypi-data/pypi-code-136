import altair as alt
alt.themes.enable("weanalyze")


def plot_ts_line(source,x,y,color,x_title,y_title,title,beta=0,y_label_expr=None,width=600,height=300):
    # Create a line hover
    hover = alt.selection_single(
        fields=[x],
        nearest=True,
        on="mouseover",
        empty="none",
        clear="mouseout"
    )
    # Prepare line plot
    # y_range = [(1-beta)*source[y].min(), (1+beta)*source[y].max()]    
    if y_label_expr is None:
        lines = alt.Chart(source).mark_line().encode(
            x=alt.X('{}:T'.format(x),axis=alt.Axis(format="%Y-%m-%d %H:%M"),title=x_title),
            # y=alt.Y('{}:Q'.format(y),scale=alt.Scale(domain=y_range),title=y_title),
            y=alt.Y('{}:Q'.format(y),title=y_title),
            color='{}:N'.format(color),
        )
    else:
        lines = alt.Chart(source).mark_line().encode(
            x=alt.X('{}:T'.format(x),axis=alt.Axis(format="%Y-%m-%d %H:%M"),title=x_title),
            # y=alt.Y('{}:Q'.format(y),axis=alt.Axis(tickCount=10,labelExpr=y_label_expr),scale=alt.Scale(domain=y_range),title=y_title),
            y=alt.Y('{}:Q'.format(y),axis=alt.Axis(tickCount=10,labelExpr=y_label_expr),title=y_title),
            color='{}:N'.format(color),
        )
    # Add hover point
    points = lines.transform_filter(hover).mark_circle()
    # Legend list
    colors = source[color].unique().tolist()
    # Tooltips
    tooltips = alt.Chart(source).transform_pivot(
        color, y, groupby=[x]
    ).mark_rule().encode(
        x='{}:T'.format(x),
        opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
        tooltip=[alt.Tooltip('{}:T'.format(x), format='%Y-%m-%d %H:%M')] + ["{}:Q".format(c) for c in colors]
    ).add_selection(hover)
    
    # Plot
    # Put the five layers into a chart and bind the data
    p = alt.layer(
        lines, points, tooltips
    ).properties(
        title=title,
        width=width, 
        height=height
    )    
    return p


def plot_bar_line(source,x,y1,y2,x_title,y1_title,y2_title,title,opacity=1,beta=0,x_format="%Y-%m-%d",width=600,height=300):
    """
    Line / Bar, dual axis
        x = 'report_date'
        y1 = 'rmb_loan_same'
        y2 = 'rmb_loan'    
        y1_title = '同比增长(%)'
        y2_title = '当月新增信贷(亿元)'
    """
    base = alt.Chart(source).encode(
        alt.X('{}:T'.format(x), axis=alt.Axis(format=x_format), title=x_title),
        tooltip=[
            alt.Tooltip('{}:T'.format(x), format=x_format), 
            alt.Tooltip('{}:Q'.format(y1)), 
            alt.Tooltip('{}:Q'.format(y2))
        ]
    )
    # Prepare data
    if beta < 0:
        y_range = [min(-10,(1-beta)*source[y1].min()), max(10,(1+beta)*source[y1].max())] 
    else:
        y_range = [(1-beta)*source[y1].min(), (1+beta)*source[y1].max()] 
    bar = base.mark_bar(opacity=opacity).encode(
        alt.Y(
            '{}'.format(y1),
            axis=alt.Axis(title=y1_title, titleColor='black'),
            scale=alt.Scale(domain=y_range)
        ),
        color=alt.condition(
            getattr(alt.datum, y1) > 0,
            alt.value("red"),  # The positive color
            alt.value("green")  # The negative color
        )    
    )
    line = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
        alt.Y(
            '{}'.format(y2),
            axis=alt.Axis(title=y2_title, titleColor='#5276A7')
        )
    )
    p = alt.layer(
        line, bar
    ).properties(
        title=title,
        width=width, 
        height=height
    ).resolve_scale(
        y = 'independent'
    )    
    return p


def plot_area_line(source,x,y,y1,y2,x_title,y_line_title,y_area_title,title,width=600,height=300):
    """
    Line with area, dual axis
        x = 'datetime'
        y = 'close'
        y1 = 'upper'
        y2 = 'lower'    
        y_line_title = '指数'
        y_area_title = '布林带'
    """    
    beta = 0.005
    y_range = [(1-beta)*source[y].min(), (1+beta)*source[y].max()]    

    base = alt.Chart(source).encode(
        alt.X('{}:T'.format(x), axis=alt.Axis(format="%Y-%m-%d %H:%M"),title=x_title),
        tooltip=[
            alt.Tooltip('{}:T'.format(x), format='%Y-%m-%d %H:%M'), 
            alt.Tooltip('{}:Q'.format(y)), 
            alt.Tooltip('{}:Q'.format(y1)), 
            alt.Tooltip('{}:Q'.format(y2))
        ]
    )

    area = base.mark_area(opacity=0.3).encode(
        alt.Y('{}:Q'.format(y1), scale=alt.Scale(domain=y_range), axis=alt.Axis(title=y_area_title, titleColor='#57A44C')),
        alt.Y2('{}:Q'.format(y2)),
        color = alt.value('#57A44C')
    )

    line = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
        alt.Y('{}:Q'.format(y), scale=alt.Scale(domain=y_range), axis=alt.Axis(title=y_line_title, titleColor='#5276A7'))
    )

    p = alt.layer(area, line).properties(
        title=title,
        width=width, 
        height=height
    ).resolve_scale(
        y = 'independent'
    )
    return p