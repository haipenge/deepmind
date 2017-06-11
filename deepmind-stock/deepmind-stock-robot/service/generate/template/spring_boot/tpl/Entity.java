package ${obj.component.package_name()}.entity;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.Set;
import java.io.Serializable;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.Table;

import com.faceye.util.annotation.GenerateEntityProperty;
/**
 * @实体名:${obj.name} ORM 实体
 * @对应数据库表:${obj.get_table_name()}
 * @author:@haipenge 
 * @联系作者:haipenge@gmail.com
 * @创建日期:${obj.get_current_date()}
 */
@Entity
@Table(name = "${obj.get_table_name()}")
public class ${obj.name} implements Serializable{
	/**
	 * 序列化ID
	 */
	private static final long serialVersionUID = 89261197117308${obj.get_serial_version_uid()}L;
	
	/**
	*主键,默认自增长
	*/
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id = null;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}
	@GenerateEntityProperty
	/**
	 * @说明:创建日期<br>
	 * @属性名: createDate<br>
	 * @类型: Date<br>
	 * @数据库字段:create_date<br>
	 * @author haipenge<br>
	 */
	@Column(name="create_date")
	@DateTimeFormat(pattern="yyyy-MM-dd hh24:mi:ss")
	private Date createDate=new Date();
	public Date getCreateDate() {
		return createDate;
	}

	public void setCreateDate(Date createDate) {
		this.createDate = createDate;
	}

}