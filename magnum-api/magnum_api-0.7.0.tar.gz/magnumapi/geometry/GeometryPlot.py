from typing import List

import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

from magnumapi.geometry.blocks.Block import Block
from magnumapi.geometry.blocks.CosThetaBlock import HomogenizedCosThetaBlock
from magnumapi.geometry.blocks.RectangularBlock import HomogenizedRectangularBlock
from magnumapi.geometry.primitives.Arc import Arc


class GeometryPlot:
    @classmethod
    def plotly_geometry_blocks(cls, geometry, figsize=(750, 750), xlim=(0, 80), ylim=(0, 80), fill_with_current=False):
        """ Method plotting blocks with plotly library

        :param figsize: size of the figure on a display
        :param xlim: limits in x-direction
        :param ylim: limits in y-direction
        """
        go_scatters = cls._create_plotly_scatters(geometry.blocks, fill_with_current)

        fig = go.Figure(go_scatters)
        fig.update_layout(
            autosize=False,
            width=figsize[0],
            height=figsize[1],
            yaxis_range=ylim,
            xaxis_range=xlim,
            showlegend=False,
            plot_bgcolor="rgba(0,0,0,0)"
        )
        fig.add_trace(px.scatter(x=[0], y=[0]).data[0])
        fig.update_xaxes(title=dict(text="x, [mm]"))
        fig.update_yaxes(title=dict(text="y, [mm]"))
        fig.show()

    @staticmethod
    def _create_plotly_scatters(blocks: List[Block], fill_with_current=False) -> List[go.Scatter]:
        """ Static method creating a list of plotly scatter instances

        :param blocks: list of blocks to convert to plotly scatter
        :return: a list of plotly scatter instances
        """
        go_scatter = []
        index = 1
        for block in blocks:
            if fill_with_current:
                fillcolor = "red" if block.block_def.current > 0 else "blue"
                scatter_line_color = fillcolor
            else:
                fillcolor = "white"
                scatter_line_color = "blue"
            
            for area in block.areas:
                x = [line.p1.x for line in area.lines]
                y = [line.p1.y for line in area.lines]
                x.append(area.get_line(0).p1.x)
                y.append(area.get_line(0).p1.y)

                go_scatter.append(go.Scatter(x=x, y=y, fill="toself", fillcolor=fillcolor, marker=dict(size=1),
                                             name="turn" + str(index), line=go.scatter.Line(color=scatter_line_color)))
                index += 1

        return go_scatter

    @staticmethod
    def plot_blocks(geometry, figsize=(10, 10), is_grid=True, xlim=(0, 80), ylim=(0, 80)) -> None:
        """ Method plotting all blocks with matplotlib library

        :param figsize: size of a figure on a screen
        :param is_grid: if True, then the grid is displayed, otherwise False
        :param xlim: limits in x-direction
        :param ylim: limits in y-direction
        """
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.grid(is_grid)

        for block in geometry.blocks:
            block.plot_block(ax)

        plt.show()

    @staticmethod
    def plot_bare_blocks(geometry, figsize=(15, 15), is_grid=True, xlim=(0, 80), ylim=(0, 80)) -> None:
        """ Method plotting bare (uninsulated) areas for all blocks in a geometry

        :param figsize: size of a figure on a screen
        :param is_grid: if True, then the grid is displayed, otherwise False
        :param xlim: limits in x-direction
        :param ylim: limits in y-direction
        """
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_aspect("equal", "box")
        ax.grid(is_grid)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        for block in geometry.blocks:
            block.plot_bare_block(ax)

        plt.show()

    @staticmethod
    def plotly_homogenized_geometry_blocks(geometry, figsize=(65, 65), xlim=(0, 80), ylim=(0, 80)):

        lines = []
        arcs = []

        index = 1
        for block in geometry.blocks:
            line_bottom = block.areas[0].get_line(0)
            line_top = block.areas[0].get_line(2)

            if isinstance(block, HomogenizedCosThetaBlock):
                arc_outer = block.areas[0].get_line(1)
                arc_inner = block.areas[0].get_line(3)
                arcs.append(dict(type="path",
                                 path=Arc.describe_ellipse_arc(a=arc_inner.get_radius(),
                                                               b=arc_inner.get_radius(),
                                                               start_angle=arc_inner.get_start_angle_in_rad(),
                                                               end_angle=arc_inner.get_end_angle_in_rad()),
                                 line_color="black"))

                arcs.append(dict(type="path",
                                 path=Arc.describe_ellipse_arc(a=arc_outer.get_radius(),
                                                               b=arc_outer.get_radius(),
                                                               start_angle=arc_outer.get_start_angle_in_rad(),
                                                               end_angle=arc_outer.get_end_angle_in_rad()),
                                 line_color="black"))
            elif isinstance(block, HomogenizedRectangularBlock):
                line_outer = block.areas[0].get_line(1)
                line_inner = block.areas[0].get_line(3)
                lines.append(go.Scatter(x=[line_outer.p1.x, line_outer.p2.x],
                                        y=[line_outer.p1.y, line_outer.p2.y],
                                        fill="toself", fillcolor="white", marker=dict(size=1),
                                        name="block" + str(index), line=go.scatter.Line(color="black")))

                lines.append(go.Scatter(x=[line_inner.p1.x, line_inner.p2.x],
                                        y=[line_inner.p1.y, line_inner.p2.y],
                                        fill="toself", fillcolor="white", marker=dict(size=1),
                                        name="block" + str(index), line=go.scatter.Line(color="black")))

            lines.append(go.Scatter(x=[line_bottom.p1.x, line_bottom.p2.x],
                                    y=[line_bottom.p1.y, line_bottom.p2.y],
                                    fill="toself", fillcolor="white", marker=dict(size=1),
                                    name="block" + str(index), line=go.scatter.Line(color="black")))

            lines.append(go.Scatter(x=[line_top.p1.x, line_top.p2.x],
                                    y=[line_top.p1.y, line_top.p2.y],
                                    fill="toself", fillcolor="white", marker=dict(size=1),
                                    name="block" + str(index), line=go.scatter.Line(color="black")))

            index += 1

        fig = go.Figure(lines)
        fig.update_layout(
            autosize=False,
            width=figsize[0],
            height=figsize[1],
            xaxis_range=xlim,
            yaxis_range=ylim,
            showlegend=False,
            plot_bgcolor="rgba(0,0,0,0)",
            shapes=arcs
        )
        fig.add_trace(px.scatter(x=[0], y=[0]).data[0])
        fig.update_xaxes(title=dict(text="x, [mm]"))
        fig.update_yaxes(title=dict(text="y, [mm]"))
        fig.show()
